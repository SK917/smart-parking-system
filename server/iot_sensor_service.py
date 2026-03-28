from concurrent import futures

import grpc

from backend_defs import database_interface_pb2, database_interface_pb2_grpc
from backend_defs import iot_interface_pb2, iot_interface_pb2_grpc

class IoTSensorManager(iot_interface_pb2_grpc.IoT_InterfaceServicer):
    def __init__(self, db_target="localhost:50051"):
        self.sensors = {}
        self.db_stub = database_interface_pb2_grpc.Database_InterfaceStub(grpc.insecure_channel(db_target))

    def update_sensor(self, serial_number, occupied, context):
        print(f"Received IOT update request from IOT{serial_number}. Occupancy: {occupied}")

        # If this is the first time handeling a sensor. Do not assume state until after first DB request is done.
        if serial_number not in self.sensors:
            self.sensors[serial_number] = {"occupied": None}

        sensor = self.sensors[serial_number]
        prev_occupied = sensor["occupied"]

        # Avoid sending too many DB updates. Handle messages with same state
        if prev_occupied == occupied:
            reply = iot_interface_pb2.IoTAck(success=True, serialNumber=serial_number, stateChanged=False)
            print(f"Replying to IOT{serial_number} with:\nSuccess: {reply.success}\nSerialNumber: {reply.serialNumber}\nstateChanged: {reply.stateChanged}\nerror: '{reply.error}'")
            return reply

        try:
            spot_update_req = database_interface_pb2.spotUpdateReq(iotID=serial_number, occupied=occupied)
            response = self.db_stub.updateSpotOccupancy(spot_update_req)
            db_success = response.success
            db_code = grpc.StatusCode.OK if response.success else grpc.StatusCode.UNKNOWN
        except grpc.RpcError as e:
            db_success = False
            db_code = e.code()

        if not db_success:
            if db_code == grpc.StatusCode.NOT_FOUND:
                ack_error = f"Serial number {serial_number} does not exist in database"
            else:
                ack_error = "Internal database error"
            reply = iot_interface_pb2.IoTAck(success=False, serialNumber=serial_number, stateChanged=False, error=ack_error)
            print(f"Replying to IOT{serial_number} with:\nSuccess: {reply.success}\nSerialNumber: {reply.serialNumber}\nstateChanged: {reply.stateChanged}\nerror: '{reply.error}'")
            return reply

        sensor["occupied"] = occupied
        reply = iot_interface_pb2.IoTAck(success=True, serialNumber=serial_number, stateChanged=True)
        print(f"Replying to IOT{serial_number} with:\nSuccess: {reply.success}\nSerialNumber: {reply.serialNumber}\nstateChanged: {reply.stateChanged}\nerror: '{reply.error}'")
        return reply

    def reportFree(self, request, context):
        return self.update_sensor(request.serialNumber, occupied=False, context=context)

    def reportOccupied(self, request, context):
        return self.update_sensor(request.serialNumber, occupied=True, context=context)

def serve(host="0.0.0.0", port=50053, db_target="localhost:50051"):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    iot_interface_pb2_grpc.add_IoT_InterfaceServicer_to_server(IoTSensorManager(db_target=db_target), server)
    server.add_insecure_port(f"{host}:{port}")
    server.start()
    print(f"IOT Service running on {host}:{port}")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()