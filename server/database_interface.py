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
        # returns a list of spots in a lot that have not been reserved and are not currently occupied as a JSON

        # sql stuff
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        cur.execute(
            "DELETE FROM reservations WHERE endDateTime<=? AND payment_status!='complete' AND spotID IN (SELECT spotID FROM spots WHERE occupied=false)",
            (request.datetime,)
        )
        conn.commit()

        data = {"lID": request.lotID, "now": request.datetime}
        free_spots = cur.execute("SELECT * FROM spots WHERE lotID=:lID AND occupied=false AND spotID NOT IN (SELECT spotID FROM reservations WHERE endDateTime>:now AND payment_status!='complete')", data).fetchall()
        totalSpotsRow = cur.execute("SELECT total_spots FROM parkinglots WHERE lotID=?", (request.lotID,)).fetchone()
        spotsDict = {"lotID": request.lotID, "totalSpots": totalSpotsRow[0] if totalSpotsRow else 0, "spots": []}

        for nextSpot in free_spots:
            spotsDict["spots"].append({"spotID": nextSpot[0], "occupied": nextSpot[1], "lotID": nextSpot[2]})
        reply = database_interface_pb2.AvailableSpotsResp(availableSpots=json.dumps(spotsDict, indent=4))
        return reply

    def updateReservations(self, request, context):

        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        # handle delete request
        if request.delete:
            cur.execute(
                "DELETE FROM reservations WHERE resID=:res",
                {"res": request.resID}
            )

            conn.commit()
            conn.close()

            return database_interface_pb2.UpdateResResp(
                success=True,
                resID=request.resID
            )

        cur.execute(
            "DELETE FROM reservations WHERE endDateTime<=? AND payment_status!='complete' AND spotID IN (SELECT spotID FROM spots WHERE occupied=false)",
            (request.datetime,)
        )

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
            existing = cur.execute(
                "SELECT resID FROM reservations WHERE resID=:res",
                {"res": request.resID}
            )
            row = existing.fetchone()

        if row is not None:
            # UPDATE
            data = {
                "plate": request.plateNum,
                "lot": request.lotID,
                "spot": request.spotID,
                "sDT": request.datetime,
                "eDT": endDateTime,
                "dur": request.duration,
                "res": request.resID,
                "price": request.price if request.HasField("price") else 0
            }

            if request.HasField("price"):
                cur.execute("""
                    UPDATE reservations
                    SET plateNum=:plate,
                        lotID=:lot,
                        spotID=:spot,
                        startDateTime=:sDT,
                        endDateTime=:eDT,
                        duration_min=:dur,
                        totalPayment=:price
                    WHERE resID=:res
                """, data)
            else:
                cur.execute("""
                    UPDATE reservations
                    SET plateNum=:plate,
                        lotID=:lot,
                        spotID=:spot,
                        startDateTime=:sDT,
                        endDateTime=:eDT,
                        duration_min=:dur
                    WHERE resID=:res
                """, data)

            saved_res_id = request.resID

        else:
            # INSERT
            data = {
                "plate": request.plateNum,
                "lot": request.lotID,
                "spot": request.spotID,
                "sDT": request.datetime,
                "eDT": endDateTime,
                "dur": request.duration,
                "status": "pending",
                "price": request.price if request.HasField("price") else 0
            }

            if request.HasField("resID"):
                data["res"] = request.resID
                cur.execute("""
                    INSERT INTO reservations (
                        resID, plateNum, lotID, spotID,
                        startDateTime, endDateTime,
                        duration_min, totalPayment, payment_status
                    )
                    VALUES (
                        :res, :plate, :lot, :spot,
                        :sDT, :eDT,
                        :dur, :price, :status
                    )
                """, data)
                saved_res_id = request.resID
            else:
                cur.execute("""
                    INSERT INTO reservations (
                        plateNum, lotID, spotID,
                        startDateTime, endDateTime,
                        duration_min, totalPayment, payment_status
                    )
                    VALUES (
                        :plate, :lot, :spot,
                        :sDT, :eDT,
                        :dur, :price, :status
                    )
                """, data)
                saved_res_id = cur.lastrowid

        conn.commit()
        conn.close()

        return database_interface_pb2.UpdateResResp(
            success=True,
            resID=saved_res_id
        )

    def getReservations(self, request, context):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        # gets reservations made under the platnumber
        # if resID is filled, returns just that reservation.
        if request.HasField("resID"):
            params = {"res": request.resID, "plate": request.plateNum}
            reservations = cur.execute("SELECT * FROM reservations WHERE resID=:res and plateNum=:plate", params)
        else:
            params = {"plate": request.plateNum}
            reservations = cur.execute("SELECT * FROM reservations WHERE plateNum=:plate", params)

        resDict = {"plateNum": request.plateNum, "reservations": []}

        nextRes = reservations.fetchone()
        while nextRes != None:
            resDict["reservations"].append({"resID": nextRes[0], "plateNum": nextRes[1], "lotID": nextRes[2], "spotID": nextRes[3], "startDateTime": nextRes[4], "endDateTime": nextRes[5], "duration": nextRes[6], "totalPayment": nextRes[7], "paymentStatus": nextRes[8]})
            nextRes = reservations.fetchone()
        reply = database_interface_pb2.GetResResp(reservations=json.dumps(resDict, indent=4))
        return reply

    def createTransaction(self, request, context):
        # create a new transaction entry with the relevant info
        # if the transaction is a success, go to the associated reservation and update its payment status to complete
        # return success/fail
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
    
        data = {
            "val": request.val,
            "plate": request.plateNum,
            "res": request.resID,
            "success": int(request.success),
            "method": request.paymentMethod
        }
    
        # insert transaction
        cur.execute("""
            INSERT INTO transactions (value, plate_number, resID, success, method)
            VALUES (:val, :plate, :res, :success, :method)
        """, data)
    
        trans_id = cur.lastrowid

        # if successful, update reservation payment status
        if request.success:
            cur.execute("""
                UPDATE reservations
                SET payment_status = :status
                WHERE resID = :res
            """, {
                "status": "paid",
                "res": request.resID
            })

        conn.commit()
        conn.close()

        return database_interface_pb2.TransCreateResp(
            transID=trans_id,
            success=True
        )

    def getTransactions(self, request, context):
        # check which entries are filled in the request
        # If the user ID is filled, return all transactions made by the user
        # If the resID is filled, return the transactions associated with that reservation
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
    
        if request.resID != None and request.plateNum:
            params = {"res": request.resID, "plate": request.plateNum}
            results = cur.execute(
                "SELECT * FROM transactions WHERE resID=:res AND plate_number=:plate",
                params
            )
    
        elif request.resID != None:
            params = {"res": request.resID}
            results = cur.execute(
                "SELECT * FROM transactions WHERE resID=:res",
                params
            )
    
        elif request.plateNum:
            params = {"plate": request.plateNum}
            results = cur.execute(
                "SELECT * FROM transactions WHERE plate_number=:plate",
                params
            )
    
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
    
        reply = database_interface_pb2.TransGetResp(
            transactions=json.dumps(transDict, indent=4)
        )
    
        return reply

    def updateSpotOccupancy(self, request, context):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        sensor_col = "sensorID"

        print(f"Received updateSpotOccupancy request from IoT({request.iotID}) setting occupancy to {request.occupied}")

        row = cur.execute(f"SELECT spotID, lotID, occupied FROM spots WHERE {sensor_col}=?", (request.iotID,)).fetchone()

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
            cur.execute(
                "UPDATE reservations SET payment_status='complete' WHERE spotID=? AND endDateTime>=? AND payment_status!='complete'",
                (spot, now_string)
            )

        cur.execute(f"UPDATE spots SET occupied=? WHERE {sensor_col}=?", (new_occupied, request.iotID))
        conn.commit()

        # For debug purposes I added this print that reads back the data
        try:
            row = cur.execute(f"SELECT * FROM spots WHERE {sensor_col}=?", (request.iotID,)).fetchone()
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
