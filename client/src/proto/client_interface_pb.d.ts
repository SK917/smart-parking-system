import * as jspb from 'google-protobuf'



export class AvailablespotReq extends jspb.Message {
  getLotid(): string;
  setLotid(value: string): AvailablespotReq;
  hasLotid(): boolean;
  clearLotid(): AvailablespotReq;

  getDatetime(): string;
  setDatetime(value: string): AvailablespotReq;
  hasDatetime(): boolean;
  clearDatetime(): AvailablespotReq;

  getDuration(): number;
  setDuration(value: number): AvailablespotReq;
  hasDuration(): boolean;
  clearDuration(): AvailablespotReq;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AvailablespotReq.AsObject;
  static toObject(includeInstance: boolean, msg: AvailablespotReq): AvailablespotReq.AsObject;
  static serializeBinaryToWriter(message: AvailablespotReq, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AvailablespotReq;
  static deserializeBinaryFromReader(message: AvailablespotReq, reader: jspb.BinaryReader): AvailablespotReq;
}

export namespace AvailablespotReq {
  export type AsObject = {
    lotid?: string;
    datetime?: string;
    duration?: number;
  };
}

export class AvailablespotResp extends jspb.Message {
  getAvailablespots(): string;
  setAvailablespots(value: string): AvailablespotResp;
  hasAvailablespots(): boolean;
  clearAvailablespots(): AvailablespotResp;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AvailablespotResp.AsObject;
  static toObject(includeInstance: boolean, msg: AvailablespotResp): AvailablespotResp.AsObject;
  static serializeBinaryToWriter(message: AvailablespotResp, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AvailablespotResp;
  static deserializeBinaryFromReader(message: AvailablespotResp, reader: jspb.BinaryReader): AvailablespotResp;
}

export namespace AvailablespotResp {
  export type AsObject = {
    availablespots?: string;
  };
}

export class ResReq extends jspb.Message {
  getLotid(): string;
  setLotid(value: string): ResReq;
  hasLotid(): boolean;
  clearLotid(): ResReq;

  getSpotid(): string;
  setSpotid(value: string): ResReq;
  hasSpotid(): boolean;
  clearSpotid(): ResReq;

  getUid(): string;
  setUid(value: string): ResReq;
  hasUid(): boolean;
  clearUid(): ResReq;

  getPaymentinfo(): string;
  setPaymentinfo(value: string): ResReq;
  hasPaymentinfo(): boolean;
  clearPaymentinfo(): ResReq;

  getDatetime(): string;
  setDatetime(value: string): ResReq;
  hasDatetime(): boolean;
  clearDatetime(): ResReq;

  getDuration(): string;
  setDuration(value: string): ResReq;
  hasDuration(): boolean;
  clearDuration(): ResReq;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ResReq.AsObject;
  static toObject(includeInstance: boolean, msg: ResReq): ResReq.AsObject;
  static serializeBinaryToWriter(message: ResReq, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ResReq;
  static deserializeBinaryFromReader(message: ResReq, reader: jspb.BinaryReader): ResReq;
}

export namespace ResReq {
  export type AsObject = {
    lotid?: string;
    spotid?: string;
    uid?: string;
    paymentinfo?: string;
    datetime?: string;
    duration?: string;
  };
}

export class ResResp extends jspb.Message {
  getSuccess(): boolean;
  setSuccess(value: boolean): ResResp;
  hasSuccess(): boolean;
  clearSuccess(): ResResp;

  getResid(): string;
  setResid(value: string): ResResp;
  hasResid(): boolean;
  clearResid(): ResResp;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ResResp.AsObject;
  static toObject(includeInstance: boolean, msg: ResResp): ResResp.AsObject;
  static serializeBinaryToWriter(message: ResResp, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ResResp;
  static deserializeBinaryFromReader(message: ResResp, reader: jspb.BinaryReader): ResResp;
}

export namespace ResResp {
  export type AsObject = {
    success?: boolean;
    resid?: string;
  };
}

