import * as jspb from 'google-protobuf'



export class transReq extends jspb.Message {
  getResid(): string;
  setResid(value: string): transReq;
  hasResid(): boolean;
  clearResid(): transReq;

  getPaymentinfo(): string;
  setPaymentinfo(value: string): transReq;
  hasPaymentinfo(): boolean;
  clearPaymentinfo(): transReq;

  getUid(): string;
  setUid(value: string): transReq;
  hasUid(): boolean;
  clearUid(): transReq;

  getVal(): string;
  setVal(value: string): transReq;
  hasVal(): boolean;
  clearVal(): transReq;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): transReq.AsObject;
  static toObject(includeInstance: boolean, msg: transReq): transReq.AsObject;
  static serializeBinaryToWriter(message: transReq, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): transReq;
  static deserializeBinaryFromReader(message: transReq, reader: jspb.BinaryReader): transReq;
}

export namespace transReq {
  export type AsObject = {
    resid?: string;
    paymentinfo?: string;
    uid?: string;
    val?: string;
  };
}

export class transResp extends jspb.Message {
  getResid(): string;
  setResid(value: string): transResp;
  hasResid(): boolean;
  clearResid(): transResp;

  getTransid(): string;
  setTransid(value: string): transResp;
  hasTransid(): boolean;
  clearTransid(): transResp;

  getUid(): string;
  setUid(value: string): transResp;
  hasUid(): boolean;
  clearUid(): transResp;

  getSuccess(): boolean;
  setSuccess(value: boolean): transResp;
  hasSuccess(): boolean;
  clearSuccess(): transResp;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): transResp.AsObject;
  static toObject(includeInstance: boolean, msg: transResp): transResp.AsObject;
  static serializeBinaryToWriter(message: transResp, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): transResp;
  static deserializeBinaryFromReader(message: transResp, reader: jspb.BinaryReader): transResp;
}

export namespace transResp {
  export type AsObject = {
    resid?: string;
    transid?: string;
    uid?: string;
    success?: boolean;
  };
}

