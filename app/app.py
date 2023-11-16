"""Faust consumer app."""

from google.protobuf.json_format import MessageToJson
from loguru import logger as log

from .broker import app
from .topic_greetings import greetings_topic, GreetingTBuilder


def main() -> None:
    """Main entry point."""

    # create topic greetings first by running e.g.:
    #   ( go install github.com/fgeller/jsonify@latest )
    #   ( go install github.com/fgeller/kt/v14@latest )
    # kt admin -createtopic greetings -topicdetail \
    #   <(jsonify =NumPartitions 1 =ReplicationFactor 1)

    log.info("Starting app")
    try:
        app.main()
    finally:
        log.info("App finished")


@app.agent(greetings_topic)
async def consume_greetings(my_topic):
    """Consume greeting messages from topic."""
    async for event in my_topic:
        print(MessageToJson(event))


@app.timer(5)
async def produce_greetings():
    """Produce greeting messages to topic."""
    for idx in range(10):
        data = GreetingTBuilder(message=f"Greetings! (#{idx})", idx=idx)
        log.info(f"Sending '{data.message}'")
        log.info(data.SerializeToString().decode("utf-8"))
        await consume_greetings.send(value=data)


if __name__ == "__main__":
    main()
