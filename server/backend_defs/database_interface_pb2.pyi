from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AvailableSpotsReq(_message.Message):
    __slots__ = ("lotID",)
    LOTID_FIELD_NUMBER: _ClassVar[int]
    lotID: str
    def __init__(self, lotID: _Optional[str] = ...) -> None: ...

class AvailableSpotsResp(_message.Message):
    __slots__ = ("availableSpots",)
    AVAILABLESPOTS_FIELD_NUMBER: _ClassVar[int]
    availableSpots: str
    def __init__(self, availableSpots: _Optional[str] = ...) -> None: ...

class UpdateResReq(_message.Message):
    __slots__ = ("resID", "lotID", "spotID", "uID", "datetime", "duration")
    RESID_FIELD_NUMBER: _ClassVar[int]
    LOTID_FIELD_NUMBER: _ClassVar[int]
    SPOTID_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    resID: str
    lotID: str
    spotID: str
    uID: str
    datetime: str
    duration: str
    def __init__(self, resID: _Optional[str] = ..., lotID: _Optional[str] = ..., spotID: _Optional[str] = ..., uID: _Optional[str] = ..., datetime: _Optional[str] = ..., duration: _Optional[str] = ...) -> None: ...

class UpdateResResp(_message.Message):
    __slots__ = ("success", "resID")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    RESID_FIELD_NUMBER: _ClassVar[int]
    success: bool
    resID: bool
    def __init__(self, success: bool = ..., resID: bool = ...) -> None: ...

class TransUpdateReq(_message.Message):
    __slots__ = ("resID", "uID", "paymentInfo", "transID", "val")
    RESID_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    PAYMENTINFO_FIELD_NUMBER: _ClassVar[int]
    TRANSID_FIELD_NUMBER: _ClassVar[int]
    VAL_FIELD_NUMBER: _ClassVar[int]
    resID: str
    uID: str
    paymentInfo: str
    transID: str
    val: str
    def __init__(self, resID: _Optional[str] = ..., uID: _Optional[str] = ..., paymentInfo: _Optional[str] = ..., transID: _Optional[str] = ..., val: _Optional[str] = ...) -> None: ...

class TransUpdateResp(_message.Message):
    __slots__ = ("transID", "success")
    TRANSID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    transID: str
    success: bool
    def __init__(self, transID: _Optional[str] = ..., success: bool = ...) -> None: ...
