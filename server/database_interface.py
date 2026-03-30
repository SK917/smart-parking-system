from concurrent import futures
import grpc
import sqlite3
import math
import datetime
from backend_defs import client_interface_pb2_grpc, client_interface_pb2
from backend_defs import database_interface_pb2_grpc, database_interface_pb2
from backend_defs import pricing_calculator_pb2_grpc, pricing_calculator_pb2
from backend_defs import transaction_handler_pb2_grpc, transaction_handler_pb2
import json

class databaseInterface(database_interface_pb2_grpc.Database_InterfaceServicer):
    def __init__(self):
        self.db_path = "../database/parkinglot.db"

    def getAvailableSpots(self, request, context):
        print(f"[getAvailableSpots] Received Request With: Lot ID({request.lotID}), Datetime({request.datetime})")
        # returns a list of spots in a lot that have not been reserved and are not currently occupied as a JSON

        # sql stuff
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        # delete reservations that have expired (L + ratio)
        now_string = request.datetime.replace("'", "''")
        cur.execute(f"DELETE FROM reservations WHERE endDateTime<='{now_string}' AND payment_status!='complete' AND spotID IN (SELECT spotID FROM spots WHERE occupied=false)")
        conn.commit()

        free_spots = cur.execute(f"SELECT * FROM spots WHERE lotID={request.lotID} AND occupied=false AND spotID NOT IN (SELECT spotID FROM reservations WHERE endDateTime>'{now_string}' AND payment_status!='complete')").fetchall()
        totalSpotsRow = cur.execute(f"SELECT total_spots FROM parkinglots WHERE lotID={request.lotID}").fetchone()
        spotsDict = {"lotID": request.lotID, "totalSpots": totalSpotsRow[0] if totalSpotsRow else 0, "spots": []}

        for nextSpot in free_spots:
            spotsDict["spots"].append({"spotID": nextSpot[0], "occupied": nextSpot[1], "lotID": nextSpot[2]})
        reply = database_interface_pb2.AvailableSpotsResp(availableSpots=json.dumps(spotsDict, indent=4))
        print(f"[getAvailableSpots] response: Remaining({len(spotsDict['spots'])}), Total({spotsDict['totalSpots']})")
        return reply

    def updateReservations(self, request, context):
        print(f"[updateReservations] Received Request With: Reservation ID({request.resID if request.HasField('resID') else 'new'}), Lot ID({request.lotID if request.HasField('lotID') else 'none'}), Spot ID({request.spotID if request.HasField('spotID') else 'none'}), Cancel({request.delete})")

        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        # handle delete request
        if request.delete:
            cur.execute(f"DELETE FROM reservations WHERE resID={request.resID}")
            print(f"[updateReservations] delete: Reservation ID({request.resID})")

            conn.commit()
            conn.close()

            return database_interface_pb2.UpdateResResp(success=True, resID=request.resID)

        now_string = request.datetime.replace("'", "''")
        cur.execute(f"DELETE FROM reservations WHERE endDateTime<='{now_string}' AND payment_status!='complete' AND spotID IN (SELECT spotID FROM spots WHERE occupied=false)")

        # parse datetime
        date = request.datetime.split(" ")[0].split("-")
        startHour = int(request.datetime.split(" ")[1].split(":")[0])
        startMin = int(request.datetime.split(" ")[1].split(":")[1])

        endHour = startHour + (request.duration // 60)
        endMin = startMin + (request.duration % 60)

        if endMin >= 60:
            endHour += 1
            endMin -= 60

        if endHour > 23:
            endDay = int(date[2]) + 1
            endHour -= 24
        else:
            endDay = date[2]

        endDateTime = f"{date[0]}-{date[1]}-{endDay} {endHour}:{endMin}:00"

        # check if reservation exists
        row = None
        if request.HasField("resID"):
            existing = cur.execute(f"SELECT resID FROM reservations WHERE resID={request.resID}")
            row = existing.fetchone()

        if row is not None:
            # UPDATE
            plate = request.plateNum.replace("'", "''")
            sdt = request.datetime.replace("'", "''")
            edt = endDateTime.replace("'", "''")

            if request.HasField("price"):
                cur.execute(f"UPDATE reservations SET plateNum='{plate}', lotID={request.lotID}, spotID={request.spotID}, startDateTime='{sdt}', endDateTime='{edt}', duration_min={request.duration}, totalPayment={request.price} WHERE resID={request.resID}")
            else:
                cur.execute(f"UPDATE reservations SET plateNum='{plate}', lotID={request.lotID}, spotID={request.spotID}, startDateTime='{sdt}', endDateTime='{edt}', duration_min={request.duration} WHERE resID={request.resID}")

            saved_res_id = request.resID
            print(f"[updateReservations] updated: Reservation ID({saved_res_id}), End Datetime({endDateTime})")

        else:
            # INSERT
            plate = request.plateNum.replace("'", "''")
            sdt = request.datetime.replace("'", "''")
            edt = endDateTime.replace("'", "''")
            price = request.price if request.HasField("price") else 0

            if request.HasField("resID"):
                cur.execute(f"INSERT INTO reservations (resID, plateNum, lotID, spotID, startDateTime, endDateTime, duration_min, totalPayment, payment_status) VALUES ({request.resID}, '{plate}', {request.lotID}, {request.spotID}, '{sdt}', '{edt}', {request.duration}, {price}, 'pending')")
                saved_res_id = request.resID
            else:
                cur.execute(f"INSERT INTO reservations (plateNum, lotID, spotID, startDateTime, endDateTime, duration_min, totalPayment, payment_status) VALUES ('{plate}', {request.lotID}, {request.spotID}, '{sdt}', '{edt}', {request.duration}, {price}, 'pending')")
                saved_res_id = cur.lastrowid
            print(f"[updateReservations] inserted: Reservation ID({saved_res_id}), End Datetime({endDateTime}), Price({price})")

        conn.commit()
        conn.close()

        print(f"[updateReservations] response: Success(True), Reservation ID({saved_res_id})")
        return database_interface_pb2.UpdateResResp(success=True, resID=saved_res_id)

    def getReservations(self, request, context):
        # TODO: Gotta update this for the new search
        print(f"[getReservations] Received Request With: Plate({request.plateNum}), Reservation ID({request.resID if request.HasField('resID') else 'all'})")
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        # gets reservations made under the platnumber
        # if resID is filled, returns just that reservation.
        plate = request.plateNum.replace("'", "''")
        if request.HasField("resID"):
            reservations = cur.execute(f"SELECT * FROM reservations WHERE resID={request.resID} and plateNum='{plate}'")
        else:
            reservations = cur.execute(f"SELECT * FROM reservations WHERE plateNum='{plate}'")

        resDict = {"plateNum": request.plateNum, "reservations": []}

        nextRes = reservations.fetchone()
        while nextRes != None:
            resDict["reservations"].append({"resID": nextRes[0], "plateNum": nextRes[1], "lotID": nextRes[2], "spotID": nextRes[3], "startDateTime": nextRes[4], "endDateTime": nextRes[5], "duration": nextRes[6], "totalPayment": nextRes[7], "paymentStatus": nextRes[8]})
            nextRes = reservations.fetchone()
        reply = database_interface_pb2.GetResResp(reservations=json.dumps(resDict, indent=4))
        print(f"[getReservations] response: Count({len(resDict['reservations'])})")
        return reply

    def createTransaction(self, request, context):
        print(f"[createTransaction] Received Request With: Reservation ID({request.resID}), Plate({request.plateNum}), Value({request.val}), Success({request.success}), Payment Method({request.paymentMethod})")
        # create a new transaction entry with the relevant info
        # if the transaction is a success, go to the associated reservation and update its payment status to complete
        # return success/fail
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        plate = request.plateNum.replace("'", "''")
        method = request.paymentMethod.replace("'", "''")

        # insert transaction
        cur.execute(f"INSERT INTO transactions (value, plate_number, resID, success, method) VALUES ({request.val}, '{plate}', {request.resID}, {int(request.success)}, '{method}')")

        trans_id = cur.lastrowid

        # if successful, update reservation payment status
        if request.success:
            cur.execute(f"UPDATE reservations SET payment_status='paid' WHERE resID={request.resID}")

        conn.commit()
        conn.close()

        print(f"[createTransaction] response: Transaction ID({trans_id}), Success(True)")
        return database_interface_pb2.TransCreateResp(transID=trans_id, success=True)

    def getTransactions(self, request, context):
        print(f"[getTransactions] Received Request With: Plate({request.plateNum if request.plateNum else 'none'}), Reservation ID({request.resID if request.resID != None else 'none'})")
        # check which entries are filled in the request
        # If the user ID is filled, return all transactions made by the user
        # If the resID is filled, return the transactions associated with that reservation
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        plate = request.plateNum.replace("'", "''")

        if request.resID != None and request.plateNum:
            results = cur.execute(f"SELECT * FROM transactions WHERE resID={request.resID} AND plate_number='{plate}'")

        elif request.resID != None:
            results = cur.execute(f"SELECT * FROM transactions WHERE resID={request.resID}")

        elif request.plateNum:
            results = cur.execute(f"SELECT * FROM transactions WHERE plate_number='{plate}'")
        else:
            results = cur.execute("SELECT * FROM transactions")

        transDict = {"transactions": []}

        nextTrans = results.fetchone()
        while nextTrans != None:
            transDict["transactions"].append({
                "transactionID": nextTrans[0],
                "value": nextTrans[1],
                "plateNum": nextTrans[2],
                "resID": nextTrans[3],
                "success": nextTrans[4],
                "method": nextTrans[5]
            })
            nextTrans = results.fetchone()
        conn.close()

        reply = database_interface_pb2.TransGetResp(transactions=json.dumps(transDict, indent=4))

        print(f"[getTransactions] response: Count({len(transDict['transactions'])})")

        return reply

    def updateSpotOccupancy(self, request, context):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        sensor_col = "sensorID"

        print(f"Received updateSpotOccupancy request from IoT({request.iotID}) setting occupancy to {request.occupied}")

        row = cur.execute(f"SELECT spotID, lotID, occupied FROM spots WHERE {sensor_col}={request.iotID}").fetchone()

        if row is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            conn.close()
            return database_interface_pb2.spotUpdateResp(success=False)

        spot, lot, currently_occupied = row
        new_occupied = bool(request.occupied)

        old_occupied = bool(currently_occupied)

        if old_occupied == new_occupied:
            conn.close()
            return database_interface_pb2.spotUpdateResp(success=True)

        if new_occupied:
            now_string = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cur.execute(f"UPDATE reservations SET payment_status='complete' WHERE spotID={spot} AND endDateTime>='{now_string}' AND payment_status!='complete'")

        cur.execute(f"UPDATE spots SET occupied={int(new_occupied)} WHERE {sensor_col}={request.iotID}")
        conn.commit()

        # For debug purposes I added this print that reads back the data
        try:
            row = cur.execute(f"SELECT * FROM spots WHERE {sensor_col}={request.iotID}").fetchone()
            print(f"Updated spot occupancy in database. Current state for IoT({request.iotID}): {row}")
        except Exception as e:
            print(f"Error fetching updated spot occupancy for IoT({request.iotID}): {e}")

        conn.close()


        return database_interface_pb2.spotUpdateResp(success=True)

def serve(host="0.0.0.0", port=50051):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    database_interface_pb2_grpc.add_Database_InterfaceServicer_to_server(databaseInterface(), server)
    server.add_insecure_port(f"{host}:{port}")
    server.start()
    print(f"DB Interface running on {host}:{port}")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
