import { parkingClient } from "./grpc";
import { create } from "@bufbuild/protobuf";
import { AvailablespotReqSchema, ResReqSchema, ResGetReqSchema, ResEditReqSchema } from "@/proto/client_interface_pb.js";

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
    plateNum: string,
    paymentInfo: string,
    datetime: string,
    duration: number
): Promise<{ success: boolean; resID: string; errorCode?: string }> => {
    return parkingClient.makeReservation(
        create(ResReqSchema, { lotID, spotID, plateNum, paymentInfo, datetime, duration })
    ).then(response => ({
        success: response.success,
        resID: response.resID,
        errorCode: response.errorCode,
    }));
};

export const getReservations = (
    plateNum: string,
    resID?: string
): Promise<string> => {
    return parkingClient.getReservations(
        create(ResGetReqSchema, { plateNum, resID })
    ).then(response => response.reservations);
};

export const editReservation = (
    resID: string,
    datetime?: string,
    duration?: number,
    cancel?: boolean
): Promise<{ resID: string; success: boolean; errorCode?: string }> => {
    return parkingClient.editRes(
        create(ResEditReqSchema, { resID, datetime, duration, cancel })
    ).then(response => ({
        resID: response.resID,
        success: response.success,
        errorCode: response.errorCode,
    }));
};