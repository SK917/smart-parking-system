import grpc
from concurrent import futures
from backend_defs import client_interface_pb2_grpc, client_interface_pb2
from backend_defs import database_interface_pb2_grpc, database_interface_pb2
from backend_defs import pricing_calculator_pb2_grpc, pricing_calculator_pb2
from backend_defs import transaction_handler_pb2_grpc, transaction_handler_pb2
import json

T_HANDLER = None
DB_INTERFACE: database_interface_pb2_grpc.Database_InterfaceStub = None
PRICE_CALC = None


class clientInterface(client_interface_pb2_grpc.Client_InterfaceServicer):
    def getAvailablespots(self, request, context):
        # make request to database for open spots with no reservation
        spotsReq = database_interface_pb2.AvailableSpotsReq(lotID=request.lotID)
        spots = DB_INTERFACE.getAvailableSpots(spotsReq).availableSpots
        spots_dict = json.loads(spots)
        # get number of spots
        remainingSpots = len(spots_dict["spots"])
        
        # make request to pricing calculator for prices for those spots
        priceReq = pricing_calculator_pb2.PriceReq(lotID=request.lotID, spots=remainingSpots, totalSpots=spots_dict["totalSpots"], datetime=request.datetime, duration=request.duration)
        spots_dict["price"] = PRICE_CALC.getPrice(priceReq).price
        
        # return spots with their prices
        availableSpots = client_interface_pb2.AvailablespotResp(availablespots=json.dumps(spots_dict, indent=4))
        return availableSpots

    def makeReservation(self, request, context):
        # make a request to the database to check if the user already has a reservation
        resGetReq = database_interface_pb2.GetResReq(plateNum=request.plateNum)
        reservations = json.loads(DB_INTERFACE.getReservations(resGetReq).reservations)
        duplicate = False
        for r in reservations["reservations"]:
            date = r["startDateTime"].split(" ")[0].split("-")
            reqDate = request.datetime.split(" ")[0].split("-")
            if date[0] == reqDate[0] and date[1] == reqDate[1] and date[2] == reqDate[2]:
                duplicate = True
                error = "Error: User already has reservation today"
                reply = client_interface_pb2.ResResp(success=False, errorCode=error)
                return reply
        # make request to database to enter a new reservation entry or update existing entry for the requested spot
        resMakeReq = database_interface_pb2.UpdateResReq(lotID=request.lotID, spotID=request.spotID, plateNum=request.plateNum, datetime=request.datetime, duration=request.duration)
        resResp = DB_INTERFACE.updateReservations(resMakeReq)

        # make request to transaction handler to process transaction
        transReq = transaction_handler_pb2.transReq(resID=resResp.resID, paymentInfo=request.paymentInfo, plateNum=request.plateNum, val=request.price)
        transResp = T_HANDLER.makePayment(transReq)

        # return whether or not the reservation was successful
        if transResp.success == True and resResp == True:
            reply = client_interface_pb2.ResResp(success=True, resID=resResp.resID, errorCode=None)
        elif transResp.success == False and resResp == True:
            reply = client_interface_pb2.ResResp(success=True, resID=resResp.resID, errorCode=transResp.errorCode)
        elif transResp.success == True and resResp == False:
            reply = client_interface_pb2.ResResp(success=True, resID=resResp.resID, errorCode=resResp.errorCode)
        else:
            reply = client_interface_pb2.ResResp(success=True, resID=resResp.resID, errorCode=resResp.errorCode + "\n" + transResp.errorCode)
        
        return reply
    
    def getReservations(self, request, context):
        resReq = database_interface_pb2.GetResReq(request.plateNum, request.resID)
        reservations = DB_INTERFACE.getReservations(resReq).reservations
        reply = client_interface_pb2.ResGetResp(reservations=reservations)

        return reply
    
    def editRes(self, request, context):
        editReq = database_interface_pb2.UpdateResReq(resID=request.resID, datetime=request.datetime, duration=request.duration, delete=request.cancel)
        editResp = DB_INTERFACE.updateReservations(editReq)
        reply = client_interface_pb2.ResEditResp(resID=editResp.resID, success=editResp.success, errorCode=editResp.errorCode)
        return reply

# TODO: combine the launching of all backend code into one start script
if __name__ == '__main__':
    # set up stubs to talk to other backend services
    internal_channel = grpc.insecure_channel("localhost:50051")
    T_HANDLER = transaction_handler_pb2_grpc.Transaction_HandlerStub(internal_channel)
    DB_INTERFACE = database_interface_pb2_grpc.Database_InterfaceStub(internal_channel)
    PRICE_CALC = pricing_calculator_pb2_grpc.Pricing_CalculatorStub(internal_channel)

    # start the gRPC server on port 50052 so the proxy can talk to it
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    client_interface_pb2_grpc.add_Client_InterfaceServicer_to_server(clientInterface(), server)
    server.add_insecure_port("[::]:50052")
    server.start()
    print("client_interface server running on port 50052")
    server.wait_for_termination()