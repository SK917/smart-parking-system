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

    def updateUser(self, request, context):
        # check if user exists already
        # if yes, update user info
        # if no, create new user
        # return success/fail and error code
        pass

    def getUser(self, request, context):
        # get requested user info and return as JSON
        pass