import grpc
from concurrent import futures
from backend_defs import client_interface_pb2_grpc, client_interface_pb2
from backend_defs import database_interface_pb2_grpc, database_interface_pb2
from backend_defs import pricing_calculator_pb2_grpc, pricing_calculator_pb2
from backend_defs import transaction_handler_pb2_grpc, transaction_handler_pb2
import json

T_HANDLER = None
DB_INTERFACE = None
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
        # make a request to the database to check if the user has already paid for this reservation
        # make request to transaction handler to process transaction
        # make request to database to enter a new reservation entry or update existing entry for the requested spot
        # return whether or not the reservation was successful
        pass
    
    def getReservations(self, request, context):
        return super().getReservations(request, context)
    
    def editRes(self, request, context):
        return super().editRes(request, context)

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