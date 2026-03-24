from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PriceReq(_message.Message):
    __slots__ = ("lotID", "spotID")
    LOTID_FIELD_NUMBER: _ClassVar[int]
    SPOTID_FIELD_NUMBER: _ClassVar[int]
    lotID: str
    spotID: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, lotID: _Optional[str] = ..., spotID: _Optional[_Iterable[str]] = ...) -> None: ...

class PriceResp(_message.Message):
    __slots__ = ("price", "lotID", "spotID")
    PRICE_FIELD_NUMBER: _ClassVar[int]
    LOTID_FIELD_NUMBER: _ClassVar[int]
    SPOTID_FIELD_NUMBER: _ClassVar[int]
    price: _containers.RepeatedScalarFieldContainer[float]
    lotID: str
    spotID: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, price: _Optional[_Iterable[float]] = ..., lotID: _Optional[str] = ..., spotID: _Optional[_Iterable[str]] = ...) -> None: ...
