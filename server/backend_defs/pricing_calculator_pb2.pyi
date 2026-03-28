from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PriceReq(_message.Message):
    __slots__ = ("lotID", "remainingSpots", "totalSpots", "datetime", "duration")
    LOTID_FIELD_NUMBER: _ClassVar[int]
    REMAININGSPOTS_FIELD_NUMBER: _ClassVar[int]
    TOTALSPOTS_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    lotID: str
    remainingSpots: int
    totalSpots: int
    datetime: str
    duration: int
    def __init__(self, lotID: _Optional[str] = ..., remainingSpots: _Optional[int] = ..., totalSpots: _Optional[int] = ..., datetime: _Optional[str] = ..., duration: _Optional[int] = ...) -> None: ...

class PriceResp(_message.Message):
    __slots__ = ("price",)
    PRICE_FIELD_NUMBER: _ClassVar[int]
    price: float
    def __init__(self, price: _Optional[float] = ...) -> None: ...
