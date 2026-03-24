import grpc
from backend_defs import client_interface_pb2_grpc, client_interface_pb2
from backend_defs import database_interface_pb2_grpc, database_interface_pb2
from backend_defs import pricing_calculator_pb2_grpc, pricing_calculator_pb2
from backend_defs import transaction_handler_pb2_grpc, transaction_handler_pb2

class transactionHandler(transaction_handler_pb2_grpc.Transaction_HandlerServicer):
    def makePayment(self, request, context):
        # simulate an actual payment
        # send request to database interface to create new transaction entry
        # return with success/fail indicator and relevant transaction details
        return super().makePayment(request, context)