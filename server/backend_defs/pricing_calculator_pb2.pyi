from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PriceReq(_message.Message):
    __slots__ = ("lotID", "spots", "datetime", "duration")
    LOTID_FIELD_NUMBER: _ClassVar[int]
    SPOTS_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    lotID: str
    spots: _containers.RepeatedScalarFieldContainer[str]
    datetime: str
    duration: int
    def __init__(self, lotID: _Optional[str] = ..., spots: _Optional[_Iterable[str]] = ..., datetime: _Optional[str] = ..., duration: _Optional[int] = ...) -> None: ...

class PriceResp(_message.Message):
    __slots__ = ("prices",)
    PRICES_FIELD_NUMBER: _ClassVar[int]
    prices: str
    def __init__(self, prices: _Optional[str] = ...) -> None: ...
