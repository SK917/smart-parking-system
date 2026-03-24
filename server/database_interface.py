import grpc
from backend_defs import client_interface_pb2_grpc, client_interface_pb2
from backend_defs import database_interface_pb2_grpc, database_interface_pb2
from backend_defs import pricing_calculator_pb2_grpc, pricing_calculator_pb2
from backend_defs import transaction_handler_pb2_grpc, transaction_handler_pb2

class databaseInterface(database_interface_pb2_grpc.Database_InterfaceServicer):
    def getAvailableSpots(self, request, context):
        # returns a list of spots that have not been reserved and are not currently occupied
        pass

    def updateReservations(self, request, context):
        # checks if the reservation already exists in the database
        # if yes, update the reservation with the info in the request
        # if no, make a new reservation entry with the relevant information, linked to the relevant transaction
        pass
    
    def updateTransaction(self, request, context):
        # check if the transaction object already exists in the database
        # if yes, update the transaction with the relevant info
        # if no, create a new transaction object
        # return success/fail
        pass