from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class transReq(_message.Message):
    __slots__ = ("resID", "paymentInfo", "uID", "val")
    RESID_FIELD_NUMBER: _ClassVar[int]
    PAYMENTINFO_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    VAL_FIELD_NUMBER: _ClassVar[int]
    resID: str
    paymentInfo: str
    uID: str
    val: str
    def __init__(self, resID: _Optional[str] = ..., paymentInfo: _Optional[str] = ..., uID: _Optional[str] = ..., val: _Optional[str] = ...) -> None: ...

class transResp(_message.Message):
    __slots__ = ("resID", "transID", "uID", "success")
    RESID_FIELD_NUMBER: _ClassVar[int]
    TRANSID_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    resID: str
    transID: str
    uID: str
    success: bool
    def __init__(self, resID: _Optional[str] = ..., transID: _Optional[str] = ..., uID: _Optional[str] = ..., success: bool = ...) -> None: ...
