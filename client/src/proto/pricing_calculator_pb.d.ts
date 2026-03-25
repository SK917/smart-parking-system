import * as jspb from 'google-protobuf'



export class PriceReq extends jspb.Message {
  getLotid(): string;
  setLotid(value: string): PriceReq;
  hasLotid(): boolean;
  clearLotid(): PriceReq;

  getSpotsList(): Array<string>;
  setSpotsList(value: Array<string>): PriceReq;
  clearSpotsList(): PriceReq;
  addSpots(value: string, index?: number): PriceReq;

  getDatetime(): string;
  setDatetime(value: string): PriceReq;
  hasDatetime(): boolean;
  clearDatetime(): PriceReq;

  getDuration(): number;
  setDuration(value: number): PriceReq;
  hasDuration(): boolean;
  clearDuration(): PriceReq;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): PriceReq.AsObject;
  static toObject(includeInstance: boolean, msg: PriceReq): PriceReq.AsObject;
  static serializeBinaryToWriter(message: PriceReq, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): PriceReq;
  static deserializeBinaryFromReader(message: PriceReq, reader: jspb.BinaryReader): PriceReq;
}

export namespace PriceReq {
  export type AsObject = {
    lotid?: string;
    spotsList: Array<string>;
    datetime?: string;
    duration?: number;
  };
}

export class PriceResp extends jspb.Message {
  getPrices(): string;
  setPrices(value: string): PriceResp;
  hasPrices(): boolean;
  clearPrices(): PriceResp;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): PriceResp.AsObject;
  static toObject(includeInstance: boolean, msg: PriceResp): PriceResp.AsObject;
  static serializeBinaryToWriter(message: PriceResp, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): PriceResp;
  static deserializeBinaryFromReader(message: PriceResp, reader: jspb.BinaryReader): PriceResp;
}

export namespace PriceResp {
  export type AsObject = {
    prices?: string;
  };
}

