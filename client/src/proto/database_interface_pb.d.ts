import * as jspb from 'google-protobuf'



export class AvailableSpotsReq extends jspb.Message {
  getLotid(): string;
  setLotid(value: string): AvailableSpotsReq;
  hasLotid(): boolean;
  clearLotid(): AvailableSpotsReq;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AvailableSpotsReq.AsObject;
  static toObject(includeInstance: boolean, msg: AvailableSpotsReq): AvailableSpotsReq.AsObject;
  static serializeBinaryToWriter(message: AvailableSpotsReq, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AvailableSpotsReq;
  static deserializeBinaryFromReader(message: AvailableSpotsReq, reader: jspb.BinaryReader): AvailableSpotsReq;
}

export namespace AvailableSpotsReq {
  export type AsObject = {
    lotid?: string;
  };
}

export class AvailableSpotsResp extends jspb.Message {
  getAvailablespots(): string;
  setAvailablespots(value: string): AvailableSpotsResp;
  hasAvailablespots(): boolean;
  clearAvailablespots(): AvailableSpotsResp;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AvailableSpotsResp.AsObject;
  static toObject(includeInstance: boolean, msg: AvailableSpotsResp): AvailableSpotsResp.AsObject;
  static serializeBinaryToWriter(message: AvailableSpotsResp, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AvailableSpotsResp;
  static deserializeBinaryFromReader(message: AvailableSpotsResp, reader: jspb.BinaryReader): AvailableSpotsResp;
}

export namespace AvailableSpotsResp {
  export type AsObject = {
    availablespots?: string;
  };
}

export class UpdateResReq extends jspb.Message {
  getResid(): string;
  setResid(value: string): UpdateResReq;
  hasResid(): boolean;
  clearResid(): UpdateResReq;

  getLotid(): string;
  setLotid(value: string): UpdateResReq;
  hasLotid(): boolean;
  clearLotid(): UpdateResReq;

  getSpotid(): string;
  setSpotid(value: string): UpdateResReq;
  hasSpotid(): boolean;
  clearSpotid(): UpdateResReq;

  getUid(): string;
  setUid(value: string): UpdateResReq;
  hasUid(): boolean;
  clearUid(): UpdateResReq;

  getDatetime(): string;
  setDatetime(value: string): UpdateResReq;
  hasDatetime(): boolean;
  clearDatetime(): UpdateResReq;

  getDuration(): string;
  setDuration(value: string): UpdateResReq;
  hasDuration(): boolean;
  clearDuration(): UpdateResReq;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateResReq.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateResReq): UpdateResReq.AsObject;
  static serializeBinaryToWriter(message: UpdateResReq, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateResReq;
  static deserializeBinaryFromReader(message: UpdateResReq, reader: jspb.BinaryReader): UpdateResReq;
}

export namespace UpdateResReq {
  export type AsObject = {
    resid?: string;
    lotid?: string;
    spotid?: string;
    uid?: string;
    datetime?: string;
    duration?: string;
  };
}

export class UpdateResResp extends jspb.Message {
  getSuccess(): boolean;
  setSuccess(value: boolean): UpdateResResp;
  hasSuccess(): boolean;
  clearSuccess(): UpdateResResp;

  getResid(): boolean;
  setResid(value: boolean): UpdateResResp;
  hasResid(): boolean;
  clearResid(): UpdateResResp;

  getErrorcode(): string;
  setErrorcode(value: string): UpdateResResp;
  hasErrorcode(): boolean;
  clearErrorcode(): UpdateResResp;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateResResp.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateResResp): UpdateResResp.AsObject;
  static serializeBinaryToWriter(message: UpdateResResp, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateResResp;
  static deserializeBinaryFromReader(message: UpdateResResp, reader: jspb.BinaryReader): UpdateResResp;
}

export namespace UpdateResResp {
  export type AsObject = {
    success?: boolean;
    resid?: boolean;
    errorcode?: string;
  };
}

export class TransCreateReq extends jspb.Message {
  getResid(): string;
  setResid(value: string): TransCreateReq;
  hasResid(): boolean;
  clearResid(): TransCreateReq;

  getUid(): string;
  setUid(value: string): TransCreateReq;
  hasUid(): boolean;
  clearUid(): TransCreateReq;

  getPaymentmethod(): string;
  setPaymentmethod(value: string): TransCreateReq;
  hasPaymentmethod(): boolean;
  clearPaymentmethod(): TransCreateReq;

  getVal(): string;
  setVal(value: string): TransCreateReq;
  hasVal(): boolean;
  clearVal(): TransCreateReq;

  getSuccess(): boolean;
  setSuccess(value: boolean): TransCreateReq;
  hasSuccess(): boolean;
  clearSuccess(): TransCreateReq;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): TransCreateReq.AsObject;
  static toObject(includeInstance: boolean, msg: TransCreateReq): TransCreateReq.AsObject;
  static serializeBinaryToWriter(message: TransCreateReq, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): TransCreateReq;
  static deserializeBinaryFromReader(message: TransCreateReq, reader: jspb.BinaryReader): TransCreateReq;
}

export namespace TransCreateReq {
  export type AsObject = {
    resid?: string;
    uid?: string;
    paymentmethod?: string;
    val?: string;
    success?: boolean;
  };
}

export class TransCreateResp extends jspb.Message {
  getTransid(): string;
  setTransid(value: string): TransCreateResp;
  hasTransid(): boolean;
  clearTransid(): TransCreateResp;

  getSuccess(): boolean;
  setSuccess(value: boolean): TransCreateResp;
  hasSuccess(): boolean;
  clearSuccess(): TransCreateResp;

  getErrorcode(): string;
  setErrorcode(value: string): TransCreateResp;
  hasErrorcode(): boolean;
  clearErrorcode(): TransCreateResp;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): TransCreateResp.AsObject;
  static toObject(includeInstance: boolean, msg: TransCreateResp): TransCreateResp.AsObject;
  static serializeBinaryToWriter(message: TransCreateResp, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): TransCreateResp;
  static deserializeBinaryFromReader(message: TransCreateResp, reader: jspb.BinaryReader): TransCreateResp;
}

export namespace TransCreateResp {
  export type AsObject = {
    transid?: string;
    success?: boolean;
    errorcode?: string;
  };
}

export class TransGetReq extends jspb.Message {
  getUid(): string;
  setUid(value: string): TransGetReq;
  hasUid(): boolean;
  clearUid(): TransGetReq;

  getResid(): string;
  setResid(value: string): TransGetReq;
  hasResid(): boolean;
  clearResid(): TransGetReq;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): TransGetReq.AsObject;
  static toObject(includeInstance: boolean, msg: TransGetReq): TransGetReq.AsObject;
  static serializeBinaryToWriter(message: TransGetReq, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): TransGetReq;
  static deserializeBinaryFromReader(message: TransGetReq, reader: jspb.BinaryReader): TransGetReq;
}

export namespace TransGetReq {
  export type AsObject = {
    uid?: string;
    resid?: string;
  };
}

export class TransGetResp extends jspb.Message {
  getTransactions(): string;
  setTransactions(value: string): TransGetResp;
  hasTransactions(): boolean;
  clearTransactions(): TransGetResp;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): TransGetResp.AsObject;
  static toObject(includeInstance: boolean, msg: TransGetResp): TransGetResp.AsObject;
  static serializeBinaryToWriter(message: TransGetResp, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): TransGetResp;
  static deserializeBinaryFromReader(message: TransGetResp, reader: jspb.BinaryReader): TransGetResp;
}

export namespace TransGetResp {
  export type AsObject = {
    transactions?: string;
  };
}

export class userUpdateReq extends jspb.Message {
  getUid(): string;
  setUid(value: string): userUpdateReq;
  hasUid(): boolean;
  clearUid(): userUpdateReq;

  getUsername(): string;
  setUsername(value: string): userUpdateReq;
  hasUsername(): boolean;
  clearUsername(): userUpdateReq;

  getPassword(): string;
  setPassword(value: string): userUpdateReq;
  hasPassword(): boolean;
  clearPassword(): userUpdateReq;

  getEmail(): string;
  setEmail(value: string): userUpdateReq;
  hasEmail(): boolean;
  clearEmail(): userUpdateReq;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): userUpdateReq.AsObject;
  static toObject(includeInstance: boolean, msg: userUpdateReq): userUpdateReq.AsObject;
  static serializeBinaryToWriter(message: userUpdateReq, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): userUpdateReq;
  static deserializeBinaryFromReader(message: userUpdateReq, reader: jspb.BinaryReader): userUpdateReq;
}

export namespace userUpdateReq {
  export type AsObject = {
    uid?: string;
    username?: string;
    password?: string;
    email?: string;
  };
}

export class userUpdateResp extends jspb.Message {
  getSuccess(): boolean;
  setSuccess(value: boolean): userUpdateResp;
  hasSuccess(): boolean;
  clearSuccess(): userUpdateResp;

  getErrorcode(): string;
  setErrorcode(value: string): userUpdateResp;
  hasErrorcode(): boolean;
  clearErrorcode(): userUpdateResp;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): userUpdateResp.AsObject;
  static toObject(includeInstance: boolean, msg: userUpdateResp): userUpdateResp.AsObject;
  static serializeBinaryToWriter(message: userUpdateResp, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): userUpdateResp;
  static deserializeBinaryFromReader(message: userUpdateResp, reader: jspb.BinaryReader): userUpdateResp;
}

export namespace userUpdateResp {
  export type AsObject = {
    success?: boolean;
    errorcode?: string;
  };
}

export class userGetReq extends jspb.Message {
  getUsername(): string;
  setUsername(value: string): userGetReq;
  hasUsername(): boolean;
  clearUsername(): userGetReq;

  getEmail(): string;
  setEmail(value: string): userGetReq;
  hasEmail(): boolean;
  clearEmail(): userGetReq;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): userGetReq.AsObject;
  static toObject(includeInstance: boolean, msg: userGetReq): userGetReq.AsObject;
  static serializeBinaryToWriter(message: userGetReq, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): userGetReq;
  static deserializeBinaryFromReader(message: userGetReq, reader: jspb.BinaryReader): userGetReq;
}

export namespace userGetReq {
  export type AsObject = {
    username?: string;
    email?: string;
  };
}

export class userGetResp extends jspb.Message {
  getUserdata(): string;
  setUserdata(value: string): userGetResp;
  hasUserdata(): boolean;
  clearUserdata(): userGetResp;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): userGetResp.AsObject;
  static toObject(includeInstance: boolean, msg: userGetResp): userGetResp.AsObject;
  static serializeBinaryToWriter(message: userGetResp, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): userGetResp;
  static deserializeBinaryFromReader(message: userGetResp, reader: jspb.BinaryReader): userGetResp;
}

export namespace userGetResp {
  export type AsObject = {
    userdata?: string;
  };
}

