import grpc
from concurrent import futures
from backend_defs import client_interface_pb2_grpc, client_interface_pb2
from backend_defs import database_interface_pb2_grpc, database_interface_pb2
from backend_defs import pricing_calculator_pb2_grpc, pricing_calculator_pb2
from backend_defs import transaction_handler_pb2_grpc, transaction_handler_pb2
BASERATE = 2
class pricingCalculator(pricing_calculator_pb2_grpc.Pricing_CalculatorServicer):
    def getPrice(self, request, context):
        # return the price for spots in the lot based on the number of spots left and the time of day
        rate = BASERATE

        if int(request.datetime.split(" ")[1].split(":")[0]) < 8:
            rate = BASERATE*0.8 # early bird pricing
        elif int(request.datetime.split(" ")[1].split(":")[0]) > 5:
            rate = BASERATE * 00.8 # off-time pricing

        price = rate * (request.totalSpots/request.remainingSpots)* (request.duration/60)
        reply = pricing_calculator_pb2.PriceResp(price=price)

        return reply


def serve(host="0.0.0.0", port=50054):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pricing_calculator_pb2_grpc.add_Pricing_CalculatorServicer_to_server(pricingCalculator(), server)
    server.add_insecure_port(f"{host}:{port}")
    server.start()
    print(f"Pricing Calculator running on {host}:{port}")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
