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
    __slots__ = ("success", "resID", "errorCode")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    RESID_FIELD_NUMBER: _ClassVar[int]
    ERRORCODE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    resID: bool
    errorCode: str
    def __init__(self, success: bool = ..., resID: bool = ..., errorCode: _Optional[str] = ...) -> None: ...

class TransCreateReq(_message.Message):
    __slots__ = ("resID", "uID", "paymentMethod", "val", "success")
    RESID_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    PAYMENTMETHOD_FIELD_NUMBER: _ClassVar[int]
    VAL_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    resID: str
    uID: str
    paymentMethod: str
    val: str
    success: bool
    def __init__(self, resID: _Optional[str] = ..., uID: _Optional[str] = ..., paymentMethod: _Optional[str] = ..., val: _Optional[str] = ..., success: bool = ...) -> None: ...

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
    __slots__ = ("uID", "resID")
    UID_FIELD_NUMBER: _ClassVar[int]
    RESID_FIELD_NUMBER: _ClassVar[int]
    uID: str
    resID: str
    def __init__(self, uID: _Optional[str] = ..., resID: _Optional[str] = ...) -> None: ...

class TransGetResp(_message.Message):
    __slots__ = ("transactions",)
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    transactions: str
    def __init__(self, transactions: _Optional[str] = ...) -> None: ...

class userUpdateReq(_message.Message):
    __slots__ = ("uID", "username", "password", "email")
    UID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    uID: str
    username: str
    password: str
    email: str
    def __init__(self, uID: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class userUpdateResp(_message.Message):
    __slots__ = ("success", "errorCode")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERRORCODE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    errorCode: str
    def __init__(self, success: bool = ..., errorCode: _Optional[str] = ...) -> None: ...

class userGetReq(_message.Message):
    __slots__ = ("username", "email")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    username: str
    email: str
    def __init__(self, username: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class userGetResp(_message.Message):
    __slots__ = ("userData",)
    USERDATA_FIELD_NUMBER: _ClassVar[int]
    userData: str
    def __init__(self, userData: _Optional[str] = ...) -> None: ...
