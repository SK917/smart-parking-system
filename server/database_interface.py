from concurrent import futures
import grpc
import sqlite3
import math
from backend_defs import client_interface_pb2_grpc, client_interface_pb2
from backend_defs import database_interface_pb2_grpc, database_interface_pb2
from backend_defs import pricing_calculator_pb2_grpc, pricing_calculator_pb2
from backend_defs import transaction_handler_pb2_grpc, transaction_handler_pb2
import json

class databaseInterface(database_interface_pb2_grpc.Database_InterfaceServicer):
    def __init__(self):
        self.db_path = "Project/database/parkinglot.db"

    def getAvailableSpots(self, request, context):
        # returns a list of spots in a lot that have not been reserved and are not currently occupied as a JSON

        # sql stuff
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        date = request.startDateTime.split(" ")[0].split("-")
        startHour = int(request.startDateTime.split(" ")[1].split(":")[0])
        startMin = int(request.startDateTime.split(" ")[1].split(":")[1])
        endHour = startHour + math.floor(request.duration/60)
        endMin = startMin + request.duration % 60

        if endHour > 23:
            endDay = int(date.split("-")[2]) + 1
            endHour = endHour - 23
        else:
            endDay = date[2]
        endDateTime = f"{date[0]}-{date[1]}-{endDay} {endHour}:{endMin}:00"

        data = {"lID": request.lotID, "sDT": request.startDateTime, "eDT": endDateTime}
        free_spots = cur.execute("SELECT * FROM spots WHERE lotID=:lID AND occupied=false AND spotID NOT IN (SELECT spotID FROM reservations WHERE startDateTime>:eDT OR endDateTime<:sDT)", data)
        totalSpots = cur.execute("SELECT totalSpots FROM parkingLots WHERE lotID=?", (request.lotID,))
        spotsDict = {"lotID": request.lotID, "totalSpots": totalSpots.fetchone(), "spots": []}

        nextSpot = free_spots.fetchone()
        while nextSpot != None:
            spotsDict["spots"].append({"spotID": nextSpot[0], "lotID": nextSpot[1], "occupied": nextSpot[2]})
            nextSpot = free_spots.fetchone()
        reply = database_interface_pb2.AvailableSpotsResp(availableSpots=json.dumps(spotsDict, indent=4))

        return reply

    def updateReservations(self, request, context):
        # checks if the reservation already exists in the database
        # if yes, update the reservation with the info in the request
        # if no, consider it a new reservation, make a new reservation entry with the relevant information, set payment statues to pending by default
        pass

    def createTransaction(self, request, context):
        # create a new transaction entry with the relevant info
        # if the transaction is a success, go to the associated reservation and update its payment status to complete
        # return success/fail
        pass

    def getTransactions(self, request, context):
        # check which entries are filled in the request
        # If the user ID is filled, return transactions made by the user
        # If the resID is filled, return the transactions associated with that reservation
        pass

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

        cur.execute(f"UPDATE spots SET occupied=? WHERE {sensor_col}=?", (new_occupied, request.iotID))
        conn.commit()
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