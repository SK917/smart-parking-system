import { parkingClient } from "./grpc";
import { create } from "@bufbuild/protobuf";
import { AvailablespotReqSchema, ResReqSchema, ResGetReqSchema, ResEditReqSchema } from "@/proto/client_interface_pb.js";

export const getAvailableSpots = (
    lotID: number,
    datetime: string,
    duration: number
): Promise<string> => {
    return parkingClient.getAvailablespots(
        create(AvailablespotReqSchema, { lotID, datetime, duration })
    ).then(response => response.availablespots);
};

export const makeReservation = (
    lotID: number,
    spotID: number,
    plateNum: string,
    paymentInfo: string,
    datetime: string,
    duration: number,
    price: number
): Promise<{ success: boolean; resID: number; errorCode?: string }> => {
    return parkingClient.makeReservation(
        create(ResReqSchema, { lotID, spotID, plateNum, paymentInfo, datetime, duration, price })
    ).then(response => ({
        success: response.success,
        resID: response.resID,
        errorCode: response.errorCode,
    }));
};

export const getReservations = (
    plateNum: string,
    resID?: number
): Promise<string> => {
    return parkingClient.getReservations(
        create(ResGetReqSchema, { plateNum, resID })
    ).then(response => response.reservations);
};

export const editReservation = (
    resID: number,
    datetime?: string,
    duration?: number,
    cancel?: boolean
): Promise<{ resID: number; success: boolean; errorCode?: string }> => {
    return parkingClient.editRes(
        create(ResEditReqSchema, { resID, datetime, duration, cancel })
    ).then(response => ({
        resID: response.resID,
        success: response.success,
        errorCode: response.errorCode,
    }));
};