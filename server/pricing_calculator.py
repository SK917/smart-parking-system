import grpc
from concurrent import futures
from backend_defs import client_interface_pb2_grpc, client_interface_pb2
from backend_defs import database_interface_pb2_grpc, database_interface_pb2
from backend_defs import pricing_calculator_pb2_grpc, pricing_calculator_pb2
from backend_defs import transaction_handler_pb2_grpc, transaction_handler_pb2
BASERATE = 2
class pricingCalculator(pricing_calculator_pb2_grpc.Pricing_CalculatorServicer):
    def getPrice(self, request, context):
        # return the price for the selected number of 1-hour blocks
        if request.duration <= 0:
            return pricing_calculator_pb2.PriceResp(price=0)

        rate = BASERATE

        # peak hours are 9:00 to 17:59
        hour = int(request.datetime.split(" ")[1].split(":")[0])
        if hour >= 9 and hour <= 17:
            rate = BASERATE * 2

        if request.totalSpots > 0:
            availability_multiplier = 1 + (request.totalSpots / request.remainingSpots )
        else:
            availability_multiplier = 1

        price = rate * availability_multiplier * (request.duration / 60)
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
