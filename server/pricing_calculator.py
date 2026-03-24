import grpc
from backend_defs import client_interface_pb2_grpc, client_interface_pb2
from backend_defs import database_interface_pb2_grpc, database_interface_pb2
from backend_defs import pricing_calculator_pb2_grpc, pricing_calculator_pb2
from backend_defs import transaction_handler_pb2_grpc, transaction_handler_pb2

class pricingCalculator(pricing_calculator_pb2_grpc.Pricing_CalculatorServicer):
    def getPrice(self, request, context):
        # given the lot ID, get all the spots available at the time
        # based on the number of spots available, their positions, and requested duration, calculate a price for each one.
        # return the price for each lot as a JSON
        return super().getPrice(request, context)