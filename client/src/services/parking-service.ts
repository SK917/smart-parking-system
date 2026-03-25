import { parkingClient } from "./grpc";
import { AvailablespotReq, ResReq } from "@/proto/client_interface_pb";

export const getAvailableSpots = (
    lotID: string,
    datetime: string,
    duration: number
): Promise<string> => {
    return new Promise((resolve, reject) => {
        const req = new AvailablespotReq();
        req.setLotid(lotID);
        req.setDatetime(datetime);
        req.setDuration(duration);

        parkingClient.getAvailablespots(req, {}, (err, response) => {
            if (err) return reject(err);
            resolve(response.getAvailablespots());
        });
    });
};

export const makeReservation = (
    lotID: string,
    spotID: string,
    uid: string,
    paymentInfo: string,
    datetime: string,
    duration: string
): Promise<{ success: boolean; resID: string }> => {
    return new Promise((resolve, reject) => {
        const req = new ResReq();
        req.setLotid(lotID);
        req.setSpotid(spotID);
        req.setUid(uid);
        req.setPaymentinfo(paymentInfo);
        req.setDatetime(datetime);
        req.setDuration(duration);

        parkingClient.makeReservation(req, {}, (err, response) => {
            if (err) return reject(err);
            resolve({
                success: response.getSuccess(),
                resID: response.getResid(),
            });
        });
    });
};