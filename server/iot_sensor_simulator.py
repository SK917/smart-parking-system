import argparse

import grpc

from backend_defs import iot_interface_pb2, iot_interface_pb2_grpc

def send_message(stub, sensor_id, args):
    if args.free:
        free_msg = iot_interface_pb2.FreeMsg(serialNumber=sensor_id)
        response = stub.reportFree(free_msg)
        change = "free"
    elif args.occupied:
        occupied_msg = iot_interface_pb2.OccupiedMsg(serialNumber=sensor_id)
        response = stub.reportOccupied(occupied_msg)
        change = "occupied"

    if response.success:
        print(f"IoT({response.serialNumber}) has been set to {change} successfully.")
    else:
        print(f"Failed to set IoT({response.serialNumber}) to {change}. Error: {response.error}")

def main():
    parser = argparse.ArgumentParser(description="Simulate IoT parking sensor gRPC messages")
    parser.add_argument("--serial", type=int, required=True, help="sensor serial number")
    parser.add_argument("--occupied", action="store_true", help="change the spot to occupied")
    parser.add_argument("--free", action="store_true", help="change the spot to free")

    # Adding this in case TA asks us to show a service dropping (We should use the IoT service as the example)
    parser.add_argument("--iotService", type=str, default="localhost:50053", help="target address for IoT service (default: localhost:50053)")
    args = parser.parse_args()

    target = args.iotService
    with grpc.insecure_channel(target) as channel:
        stub = iot_interface_pb2_grpc.IoT_InterfaceStub(channel)
        send_message(stub, sensor_id=args.serial, args=args)

if __name__ == "__main__":
    main()