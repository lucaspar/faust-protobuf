"""Faust consumer app."""

import faust
from faust.types.topics import TopicT
from google.protobuf.json_format import MessageToJson
from loguru import logger as log

from .proto.greetings_pb2 import (  # pylint: disable=no-name-in-module
    Greeting,
)
from .proto_serializer import ProtobufSerializer

app = faust.App(
    "faust-consumer",
    broker="kafka://",
    store="memory://",
    cache="memory://",
    topic_partitions=1,
)

greetings_schema = faust.Schema(
    key_serializer=ProtobufSerializer(pb_type=Greeting),
    value_serializer=ProtobufSerializer(pb_type=Greeting),
)

TOPIC: TopicT = app.topic("greetings", schema=greetings_schema)


def main() -> None:

    # create topic greetings first by running e.g.:
    #   ( go install github.com/fgeller/jsonify@latest )
    #   ( go install github.com/fgeller/kt/v14@latest )
    # kt admin -createtopic greetings -topicdetail \
    #   <(jsonify =NumPartitions 1 =ReplicationFactor 1)

    app.main()

    for _topic in app.topics:
        log.info(_topic)


@app.agent(TOPIC)
async def consume(my_topic):
    async for event in my_topic:
        print(MessageToJson(event))


@app.timer(5)
async def produce():
    for idx in range(10):
        data = Greeting(message=f"Message #{idx}", idx=idx)
        await consume.send(value=data)


if __name__ == "__main__":
    main()
