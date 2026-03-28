from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AvailableSpotsReq(_message.Message):
    __slots__ = ("lotID", "datetime", "duration")
    LOTID_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    lotID: int
    datetime: str
    duration: int
    def __init__(self, lotID: _Optional[int] = ..., datetime: _Optional[str] = ..., duration: _Optional[int] = ...) -> None: ...

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
    resID: int
    lotID: int
    spotID: int
    plateNum: str
    datetime: str
    duration: int
    def __init__(self, resID: _Optional[int] = ..., lotID: _Optional[int] = ..., spotID: _Optional[int] = ..., plateNum: _Optional[str] = ..., datetime: _Optional[str] = ..., duration: _Optional[int] = ...) -> None: ...

class UpdateResResp(_message.Message):
    __slots__ = ("success", "resID", "errorCode")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    RESID_FIELD_NUMBER: _ClassVar[int]
    ERRORCODE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    resID: int
    errorCode: str
    def __init__(self, success: bool = ..., resID: _Optional[int] = ..., errorCode: _Optional[str] = ...) -> None: ...

class TransCreateReq(_message.Message):
    __slots__ = ("resID", "plateNum", "paymentMethod", "val", "success")
    RESID_FIELD_NUMBER: _ClassVar[int]
    PLATENUM_FIELD_NUMBER: _ClassVar[int]
    PAYMENTMETHOD_FIELD_NUMBER: _ClassVar[int]
    VAL_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    resID: int
    plateNum: str
    paymentMethod: str
    val: float
    success: bool
    def __init__(self, resID: _Optional[int] = ..., plateNum: _Optional[str] = ..., paymentMethod: _Optional[str] = ..., val: _Optional[float] = ..., success: bool = ...) -> None: ...

class TransCreateResp(_message.Message):
    __slots__ = ("transID", "success", "errorCode")
    TRANSID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERRORCODE_FIELD_NUMBER: _ClassVar[int]
    transID: int
    success: bool
    errorCode: str
    def __init__(self, transID: _Optional[int] = ..., success: bool = ..., errorCode: _Optional[str] = ...) -> None: ...

class TransGetReq(_message.Message):
    __slots__ = ("plateNum", "resID")
    PLATENUM_FIELD_NUMBER: _ClassVar[int]
    RESID_FIELD_NUMBER: _ClassVar[int]
    plateNum: str
    resID: int
    def __init__(self, plateNum: _Optional[str] = ..., resID: _Optional[int] = ...) -> None: ...

class TransGetResp(_message.Message):
    __slots__ = ("transactions",)
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    transactions: str
    def __init__(self, transactions: _Optional[str] = ...) -> None: ...

class spotUpdateReq(_message.Message):
    __slots__ = ("iotID", "occupied")
    IOTID_FIELD_NUMBER: _ClassVar[int]
    OCCUPIED_FIELD_NUMBER: _ClassVar[int]
    iotID: int
    occupied: bool
    def __init__(self, iotID: _Optional[int] = ..., occupied: bool = ...) -> None: ...

class spotUpdateResp(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class GetResReq(_message.Message):
    __slots__ = ("plateNum", "resID")
    PLATENUM_FIELD_NUMBER: _ClassVar[int]
    RESID_FIELD_NUMBER: _ClassVar[int]
    plateNum: str
    resID: int
    def __init__(self, plateNum: _Optional[str] = ..., resID: _Optional[int] = ...) -> None: ...

class GetResResp(_message.Message):
    __slots__ = ("reservations",)
    RESERVATIONS_FIELD_NUMBER: _ClassVar[int]
    reservations: str
    def __init__(self, reservations: _Optional[str] = ...) -> None: ...
