from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AvailablespotReq(_message.Message):
    __slots__ = ("lotID", "datetime", "duration")
    LOTID_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    lotID: int
    datetime: str
    duration: int
    def __init__(self, lotID: _Optional[int] = ..., datetime: _Optional[str] = ..., duration: _Optional[int] = ...) -> None: ...

class AvailablespotResp(_message.Message):
    __slots__ = ("availablespots",)
    AVAILABLESPOTS_FIELD_NUMBER: _ClassVar[int]
    availablespots: str
    def __init__(self, availablespots: _Optional[str] = ...) -> None: ...

class ResReq(_message.Message):
    __slots__ = ("lotID", "spotID", "plateNum", "paymentInfo", "datetime", "duration", "price")
    LOTID_FIELD_NUMBER: _ClassVar[int]
    SPOTID_FIELD_NUMBER: _ClassVar[int]
    PLATENUM_FIELD_NUMBER: _ClassVar[int]
    PAYMENTINFO_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    lotID: int
    spotID: int
    plateNum: str
    paymentInfo: str
    datetime: str
    duration: int
    price: float
    def __init__(self, lotID: _Optional[int] = ..., spotID: _Optional[int] = ..., plateNum: _Optional[str] = ..., paymentInfo: _Optional[str] = ..., datetime: _Optional[str] = ..., duration: _Optional[int] = ..., price: _Optional[float] = ...) -> None: ...

class ResResp(_message.Message):
    __slots__ = ("success", "resID", "errorCode")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    RESID_FIELD_NUMBER: _ClassVar[int]
    ERRORCODE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    resID: int
    errorCode: str
    def __init__(self, success: bool = ..., resID: _Optional[int] = ..., errorCode: _Optional[str] = ...) -> None: ...

class ResGetReq(_message.Message):
    __slots__ = ("plateNum", "resID")
    PLATENUM_FIELD_NUMBER: _ClassVar[int]
    RESID_FIELD_NUMBER: _ClassVar[int]
    plateNum: str
    resID: int
    def __init__(self, plateNum: _Optional[str] = ..., resID: _Optional[int] = ...) -> None: ...

class ResGetResp(_message.Message):
    __slots__ = ("reservations",)
    RESERVATIONS_FIELD_NUMBER: _ClassVar[int]
    reservations: str
    def __init__(self, reservations: _Optional[str] = ...) -> None: ...

class ResEditReq(_message.Message):
    __slots__ = ("resID", "datetime", "duration", "cancel")
    RESID_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    CANCEL_FIELD_NUMBER: _ClassVar[int]
    resID: int
    datetime: str
    duration: int
    cancel: bool
    def __init__(self, resID: _Optional[int] = ..., datetime: _Optional[str] = ..., duration: _Optional[int] = ..., cancel: bool = ...) -> None: ...

class ResEditResp(_message.Message):
    __slots__ = ("resID", "success", "errorCode")
    RESID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERRORCODE_FIELD_NUMBER: _ClassVar[int]
    resID: int
    success: bool
    errorCode: str
    def __init__(self, resID: _Optional[int] = ..., success: bool = ..., errorCode: _Optional[str] = ...) -> None: ...
