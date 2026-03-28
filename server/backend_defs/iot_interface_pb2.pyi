from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FreeMsg(_message.Message):
    __slots__ = ("serialNumber",)
    SERIALNUMBER_FIELD_NUMBER: _ClassVar[int]
    serialNumber: int
    def __init__(self, serialNumber: _Optional[int] = ...) -> None: ...

class OccupiedMsg(_message.Message):
    __slots__ = ("serialNumber",)
    SERIALNUMBER_FIELD_NUMBER: _ClassVar[int]
    serialNumber: int
    def __init__(self, serialNumber: _Optional[int] = ...) -> None: ...

class IoTAck(_message.Message):
    __slots__ = ("success", "serialNumber", "stateChanged", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    SERIALNUMBER_FIELD_NUMBER: _ClassVar[int]
    STATECHANGED_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    serialNumber: int
    stateChanged: bool
    error: str
    def __init__(self, success: bool = ..., serialNumber: _Optional[int] = ..., stateChanged: bool = ..., error: _Optional[str] = ...) -> None: ...
