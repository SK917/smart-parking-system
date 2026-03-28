from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AvailableSpotsReq(_message.Message):
    __slots__ = ("lotID", "datetime", "duration")
    LOTID_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    lotID: str
    datetime: str
    duration: int
    def __init__(self, lotID: _Optional[str] = ..., datetime: _Optional[str] = ..., duration: _Optional[int] = ...) -> None: ...

class AvailableSpotsResp(_message.Message):
    __slots__ = ("availableSpots",)
    AVAILABLESPOTS_FIELD_NUMBER: _ClassVar[int]
    availableSpots: str
    def __init__(self, availableSpots: _Optional[str] = ...) -> None: ...

class UpdateResReq(_message.Message):
    __slots__ = ("resID", "lotID", "spotID", "plateNum", "datetime", "duration")
    RESID_FIELD_NUMBER: _ClassVar[int]
    LOTID_FIELD_NUMBER: _ClassVar[int]
    SPOTID_FIELD_NUMBER: _ClassVar[int]
    PLATENUM_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    resID: str
    lotID: str
    spotID: str
    plateNum: str
    datetime: str
    duration: str
    def __init__(self, resID: _Optional[str] = ..., lotID: _Optional[str] = ..., spotID: _Optional[str] = ..., plateNum: _Optional[str] = ..., datetime: _Optional[str] = ..., duration: _Optional[str] = ...) -> None: ...

class UpdateResResp(_message.Message):
    __slots__ = ("success", "resID", "errorCode")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    RESID_FIELD_NUMBER: _ClassVar[int]
    ERRORCODE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    resID: bool
    errorCode: str
    def __init__(self, success: bool = ..., resID: bool = ..., errorCode: _Optional[str] = ...) -> None: ...

class TransCreateReq(_message.Message):
    __slots__ = ("resID", "plateNum", "paymentMethod", "val", "success")
    RESID_FIELD_NUMBER: _ClassVar[int]
    PLATENUM_FIELD_NUMBER: _ClassVar[int]
    PAYMENTMETHOD_FIELD_NUMBER: _ClassVar[int]
    VAL_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    resID: str
    plateNum: str
    paymentMethod: str
    val: float
    success: bool
    def __init__(self, resID: _Optional[str] = ..., plateNum: _Optional[str] = ..., paymentMethod: _Optional[str] = ..., val: _Optional[float] = ..., success: bool = ...) -> None: ...

class TransCreateResp(_message.Message):
    __slots__ = ("transID", "success", "errorCode")
    TRANSID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERRORCODE_FIELD_NUMBER: _ClassVar[int]
    transID: str
    success: bool
    errorCode: str
    def __init__(self, transID: _Optional[str] = ..., success: bool = ..., errorCode: _Optional[str] = ...) -> None: ...

class TransGetReq(_message.Message):
    __slots__ = ("plateNum", "resID")
    PLATENUM_FIELD_NUMBER: _ClassVar[int]
    RESID_FIELD_NUMBER: _ClassVar[int]
    plateNum: str
    resID: str
    def __init__(self, plateNum: _Optional[str] = ..., resID: _Optional[str] = ...) -> None: ...

class TransGetResp(_message.Message):
    __slots__ = ("transactions",)
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    transactions: str
    def __init__(self, transactions: _Optional[str] = ...) -> None: ...

class spotUpdateReq(_message.Message):
    __slots__ = ("spotID", "lotID", "occupied")
    SPOTID_FIELD_NUMBER: _ClassVar[int]
    LOTID_FIELD_NUMBER: _ClassVar[int]
    OCCUPIED_FIELD_NUMBER: _ClassVar[int]
    spotID: int
    lotID: int
    occupied: bool
    def __init__(self, spotID: _Optional[int] = ..., lotID: _Optional[int] = ..., occupied: bool = ...) -> None: ...

class spotUpdateResp(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...
