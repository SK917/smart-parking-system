import grpc
from concurrent import futures
from backend_defs import client_interface_pb2_grpc, client_interface_pb2
from backend_defs import database_interface_pb2_grpc, database_interface_pb2
from backend_defs import pricing_calculator_pb2_grpc, pricing_calculator_pb2
from backend_defs import transaction_handler_pb2_grpc, transaction_handler_pb2
import json
import datetime

T_HANDLER = None
DB_INTERFACE: database_interface_pb2_grpc.Database_InterfaceStub = None
PRICE_CALC = None


class clientInterface(client_interface_pb2_grpc.Client_InterfaceServicer):
    def getAvailablespots(self, request, context):
        now_string = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # make request to database for open spots with no reservation
        spotsReq = database_interface_pb2.AvailableSpotsReq(lotID=request.lotID, datetime=now_string, duration=request.duration)
        spots = DB_INTERFACE.getAvailableSpots(spotsReq).availableSpots
        spots_dict = json.loads(spots)
        # get number of spots
        remainingSpots = len(spots_dict["spots"])
        totalSpots = spots_dict["totalSpots"]

        if isinstance(totalSpots, list):
            totalSpots = totalSpots[0] if totalSpots else 0

        # make request to pricing calculator for prices for those spots
        if remainingSpots == 0:
            spots_dict["price"] = 0
        else:
            priceReq = pricing_calculator_pb2.PriceReq(lotID=request.lotID, remainingSpots=remainingSpots, totalSpots=totalSpots, datetime=now_string, duration=request.duration * 60)
            spots_dict["price"] = PRICE_CALC.getPrice(priceReq).price

        # return spots with their prices
        availableSpots = client_interface_pb2.AvailablespotResp(availablespots=json.dumps(spots_dict, indent=4))
        print(availableSpots)
        return availableSpots

    def makeReservation(self, request, context):
        now_string = request.datetime

        # make a request to the database to check if the user already has a reservation
        resGetReq = database_interface_pb2.GetResReq(plateNum=request.plateNum)
        reservations = json.loads(DB_INTERFACE.getReservations(resGetReq).reservations)
        for r in reservations["reservations"]:
            if r["paymentStatus"] != "complete" and r["endDateTime"] > now_string:
                error = "Error: User already has reservation today"
                reply = client_interface_pb2.ResResp(success=False, errorCode=error)
                return reply

        # make request to database to enter a new reservation entry or update existing entry for the requested spot
        resMakeReq = database_interface_pb2.UpdateResReq(lotID=request.lotID, spotID=request.spotID, plateNum=request.plateNum, datetime=now_string, duration=2, price=request.price)
        resResp = DB_INTERFACE.updateReservations(resMakeReq)

        if not resResp.success:
            return client_interface_pb2.ResResp(success=False, errorCode=resResp.errorCode)

        # make request to transaction handler to process transaction
        transReq = transaction_handler_pb2.transReq(resID=resResp.resID, paymentInfo=request.paymentInfo, plateNum=request.plateNum, val=request.price)
        transResp = T_HANDLER.makePayment(transReq)

        # return whether or not the reservation was successful
        if transResp.success:
            reply = client_interface_pb2.ResResp(success=True, resID=resResp.resID)
        else:
            DB_INTERFACE.updateReservations(database_interface_pb2.UpdateResReq(resID=resResp.resID, delete=True))
            reply = client_interface_pb2.ResResp(success=False, resID=resResp.resID, errorCode=transResp.errorCode)

        return reply

    def getReservations(self, request, context):
        print(f"getReservations called: {request}")
        resReq = database_interface_pb2.GetResReq(request.plateNum, request.resID)
        reservations = DB_INTERFACE.getReservations(resReq).reservations
        reply = client_interface_pb2.ResGetResp(reservations=reservations)

        return reply

    def editRes(self, request, context):
        print(f"editRes called: {request}")
        editReq = database_interface_pb2.UpdateResReq(resID=request.resID, datetime=request.datetime, duration=request.duration, delete=request.cancel)
        editResp = DB_INTERFACE.updateReservations(editReq)
        reply = client_interface_pb2.ResEditResp(resID=editResp.resID, success=editResp.success, errorCode=editResp.errorCode)
        return reply

def serve(host="0.0.0.0", port=50052, db_target="localhost:50051", pricing_target="localhost:50054", transaction_target="localhost:50055"):
    global T_HANDLER, DB_INTERFACE, PRICE_CALC

    # set up stubs to talk to other backend services
    T_HANDLER = transaction_handler_pb2_grpc.Transaction_HandlerStub(grpc.insecure_channel(transaction_target))
    DB_INTERFACE = database_interface_pb2_grpc.Database_InterfaceStub(grpc.insecure_channel(db_target))
    PRICE_CALC = pricing_calculator_pb2_grpc.Pricing_CalculatorStub(grpc.insecure_channel(pricing_target))

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    client_interface_pb2_grpc.add_Client_InterfaceServicer_to_server(clientInterface(), server)
    server.add_insecure_port(f"{host}:{port}")
    server.start()
    print(f"Client Interface running on {host}:{port}")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()