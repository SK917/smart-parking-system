import { parkingClient } from "./grpc";
import { create } from "@bufbuild/protobuf";
import { AvailablespotReqSchema, ResReqSchema } from "@/proto/client_interface_pb.js";

export const getAvailableSpots = (
    lotID: string,
    datetime: string,
    duration: number
): Promise<string> => {
    return parkingClient.getAvailablespots(
        create(AvailablespotReqSchema, { lotID, datetime, duration })
    ).then(response => response.availablespots);
};

export const makeReservation = (
    lotID: string,
    spotID: string,
    uid: string,
    paymentInfo: string,
    datetime: string,
    duration: string
): Promise<{ success: boolean; resID: string }> => {
    return parkingClient.makeReservation(
        create(ResReqSchema, { lotID, spotID, uID: uid, paymentInfo, datetime, duration })
    ).then(response => ({
        success: response.success,
        resID: response.resID,
    }));
};