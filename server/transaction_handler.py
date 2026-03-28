import grpc
from backend_defs import client_interface_pb2_grpc, client_interface_pb2
from backend_defs import database_interface_pb2_grpc, database_interface_pb2
from backend_defs import pricing_calculator_pb2_grpc, pricing_calculator_pb2
from backend_defs import transaction_handler_pb2_grpc, transaction_handler_pb2
import json

DB_INTERFACE: database_interface_pb2_grpc.Database_InterfaceStub = None

class transactionHandler(transaction_handler_pb2_grpc.Transaction_HandlerServicer):
    def makePayment(self, request, context):
        # simulate an actual payment
        # check database for info
        checkResReq = database_interface_pb2.GetResReq(plateNum=request.plateNum, resID=request.resID)
        reservation = json.dumps(DB_INTERFACE.getReservations(checkResReq).reservations)
        if reservation["reservations"][0]["paymentStatus"] == "paid":
            # already been paid, return an error.
            reply = transaction_handler_pb2.transResp(resID=request.resID, transID=None, plateNum=request.plateNum, success=False, errorCode="Error: Reservation already paid for")
            return reply
        
        
        # send request to database interface to create new transaction entry
        errCode = ""
        if request.paymentInfo == "American Express":
            suc = False
            errCode = "Error: American Express not accepted"
        else:
            suc = True
        transCreateReq = database_interface_pb2.TransCreateReq(resID=request.resID, plateNum=request.plateNum, paymentMethod=request.paymentInfo, val=request.val, success=suc)
        transCreateResp = DB_INTERFACE.createTransaction(transCreateReq)

        # return with success/fail indicator and relevant transaction details
        reply = transaction_handler_pb2.transResp(resID=request.resID, transID=transCreateResp.transID, plateNum=request.plateNum, success=(transCreateResp.success and suc), errorCode=errCode+"\n"+transCreateResp.errorCode)

        return reply