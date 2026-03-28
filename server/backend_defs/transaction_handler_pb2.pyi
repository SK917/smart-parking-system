from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class transReq(_message.Message):
    __slots__ = ("resID", "paymentInfo", "plateNum", "val")
    RESID_FIELD_NUMBER: _ClassVar[int]
    PAYMENTINFO_FIELD_NUMBER: _ClassVar[int]
    PLATENUM_FIELD_NUMBER: _ClassVar[int]
    VAL_FIELD_NUMBER: _ClassVar[int]
    resID: str
    paymentInfo: str
    plateNum: str
    val: float
    def __init__(self, resID: _Optional[str] = ..., paymentInfo: _Optional[str] = ..., plateNum: _Optional[str] = ..., val: _Optional[float] = ...) -> None: ...

class transResp(_message.Message):
    __slots__ = ("resID", "transID", "plateNum", "success")
    RESID_FIELD_NUMBER: _ClassVar[int]
    TRANSID_FIELD_NUMBER: _ClassVar[int]
    PLATENUM_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    resID: str
    transID: str
    plateNum: str
    success: bool
    def __init__(self, resID: _Optional[str] = ..., transID: _Optional[str] = ..., plateNum: _Optional[str] = ..., success: bool = ...) -> None: ...
