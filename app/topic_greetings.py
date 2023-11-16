"""Describe the topic for greeting messages."""

import faust
from faust.types.topics import TopicT

from .broker import app

from .proto.greetings_pb2 import (  # pylint: disable=no-name-in-module
    Greeting as GreetingTBuilder,  # type: ignore
)
from .proto_serializer import ProtobufSerializer

_greetings_schema = faust.Schema(
    key_serializer=ProtobufSerializer(pb_type=GreetingTBuilder),
    value_serializer=ProtobufSerializer(pb_type=GreetingTBuilder),
)

greetings_topic: TopicT = app.topic("greetings", schema=_greetings_schema)

__all__ = ["app", "greetings_topic", "GreetingTBuilder"]
