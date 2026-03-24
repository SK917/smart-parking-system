from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AvailablespotReq(_message.Message):
    __slots__ = ("lotID",)
    LOTID_FIELD_NUMBER: _ClassVar[int]
    lotID: str
    def __init__(self, lotID: _Optional[str] = ...) -> None: ...

class AvailablespotResp(_message.Message):
    __slots__ = ("availablespots",)
    AVAILABLESPOTS_FIELD_NUMBER: _ClassVar[int]
    availablespots: str
    def __init__(self, availablespots: _Optional[str] = ...) -> None: ...

class ResReq(_message.Message):
    __slots__ = ("lotID", "spotID", "uID", "paymentInfo", "datetime", "duration")
    LOTID_FIELD_NUMBER: _ClassVar[int]
    SPOTID_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    PAYMENTINFO_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    lotID: str
    spotID: str
    uID: str
    paymentInfo: str
    datetime: str
    duration: str
    def __init__(self, lotID: _Optional[str] = ..., spotID: _Optional[str] = ..., uID: _Optional[str] = ..., paymentInfo: _Optional[str] = ..., datetime: _Optional[str] = ..., duration: _Optional[str] = ...) -> None: ...

class ResResp(_message.Message):
    __slots__ = ("success", "resID")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    RESID_FIELD_NUMBER: _ClassVar[int]
    success: bool
    resID: str
    def __init__(self, success: bool = ..., resID: _Optional[str] = ...) -> None: ...
