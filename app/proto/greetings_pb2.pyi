"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Greeting(google.protobuf.message.Message):
    """A greeting represents a message you can tell a user."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IDX_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    idx: builtins.int
    message: builtins.str
    def __init__(
        self,
        *,
        idx: builtins.int = ...,
        message: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["idx", b"idx", "message", b"message"]) -> None: ...

global___Greeting = Greeting
