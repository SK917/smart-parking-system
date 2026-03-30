import grpc
from concurrent import futures
from backend_defs import client_interface_pb2_grpc, client_interface_pb2
from backend_defs import database_interface_pb2_grpc, database_interface_pb2
from backend_defs import pricing_calculator_pb2_grpc, pricing_calculator_pb2
from backend_defs import transaction_handler_pb2_grpc, transaction_handler_pb2
import json

DB_INTERFACE: database_interface_pb2_grpc.Database_InterfaceStub = None

class transactionHandler(transaction_handler_pb2_grpc.Transaction_HandlerServicer):
    def makePayment(self, request, context):
        print(f"[makePayment] Received Request With: Reservation ID({request.resID}), Plate Number({request.plateNum}), PaymentInfo({request.paymentInfo}), Value({request.val})")
        # simulate an actual payment
        # check database for info
        checkResReq = database_interface_pb2.GetResReq(plateNum=request.plateNum, resID=request.resID)
        reservations = json.loads(DB_INTERFACE.getReservations(checkResReq).reservations)
        if reservations["reservations"] and reservations["reservations"][0]["paymentStatus"] in ["paid", "complete"]:
            # already been paid, return an error.
            reply = transaction_handler_pb2.transResp(resID=request.resID, transID=None, plateNum=request.plateNum, success=False, errorCode="Error: Reservation already paid for")
            print(f"[makePayment] rejected: Error({reply.errorCode})")
            return reply

        # send request to database interface to create new transaction entry
        errCode = ""
        if request.paymentInfo.strip().lower() == "amex":
            suc = False
            errCode = "Error: American Express not accepted"
        else:
            suc = True
        transCreateReq = database_interface_pb2.TransCreateReq(resID=request.resID, plateNum=request.plateNum, paymentMethod=request.paymentInfo, val=request.val, success=suc)
        transCreateResp = DB_INTERFACE.createTransaction(transCreateReq)
        db_error = transCreateResp.errorCode if transCreateResp.errorCode else ""
        full_error = errCode
        if db_error:
            if full_error:
                full_error += "\n"
            full_error += db_error

        # return with success/fail indicator and relevant transaction details
        reply = transaction_handler_pb2.transResp(resID=request.resID, transID=transCreateResp.transID, plateNum=request.plateNum, success=(transCreateResp.success and suc), errorCode=full_error)

        if reply.success:
            print(f"[makePayment] success: Reservation ID({reply.resID}), Transaction ID({reply.transID})")
        else:
            print(f"[makePayment] failed: Reservation ID({reply.resID}), Error({reply.errorCode})")

        return reply


def serve(host="0.0.0.0", port=50055, db_target="localhost:50051"):
    global DB_INTERFACE
    DB_INTERFACE = database_interface_pb2_grpc.Database_InterfaceStub(grpc.insecure_channel(db_target))

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    transaction_handler_pb2_grpc.add_Transaction_HandlerServicer_to_server(transactionHandler(), server)
    server.add_insecure_port(f"{host}:{port}")
    server.start()
    print(f"Transaction Handler running on {host}:{port}")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()