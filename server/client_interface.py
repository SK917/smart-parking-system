import grpc
from backend_defs import client_interface_pb2_grpc, client_interface_pb2
from backend_defs import database_interface_pb2_grpc, database_interface_pb2
from backend_defs import pricing_calculator_pb2_grpc, pricing_calculator_pb2
from backend_defs import transaction_handler_pb2_grpc, transaction_handler_pb2

T_HANDLER = None
DB_INTERFACE = None
PRICE_CALC = None


class clientInterface(client_interface_pb2_grpc.Client_InterfaceServicer):
    def getAvailablespots(self, request, context):
        # make request to database for open spots with no reservation
        spotsReq = database_interface_pb2.AvailableSpotsReq(lotID=request.lotID)
        spots = DB_INTERFACE.getAvailableSpots(spotsReq).availableSpots
        # make request to pricing calculator for prices for those spots
        priceReq = pricing_calculator_pb2.PriceReq(lotID=request.lotID, spots=spots, datetime=request.datetime, duration=request.duration)
        prices = PRICE_CALC.getPrice(priceReq).prices
        # return spots with their prices
        availableSpots = client_interface_pb2.AvailablespotResp(availablespots=availableSpots)
        return availableSpots

    def makeReservation(self, request, context):
        # make a request to the database to check if the user already has a reservation
        # make a request to the database to check if the user has already paid for this reservation
        # make request to transaction handler to process transaction
        # make request to database to enter a new reservation entry or update existing entry for the requested spot
        # return whether or not the reservation was successful
        pass

# TODO: combine the launching of all backend code into one start script
if __name__ == '__main__':
    channel = grpc.insecure_channel("localhost:50051")
    T_HANDLER = transaction_handler_pb2_grpc.Transaction_HandlerStub(channel)
    DB_INTERFACE = database_interface_pb2_grpc.Database_InterfaceStub(channel)
    PRICE_CALC = pricing_calculator_pb2_grpc.Pricing_CalculatorStub(channel)