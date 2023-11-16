"""Broker initializer for Faust Streaming."""

import faust
from faust.types import AppT


def app_builder(
    broker: str = "kafka://",
    store: str = "memory://",
    cache: str = "memory://",
    topic_partitions: int = 1,
    **kwargs,
) -> faust.App:
    """Builds the Faust app."""
    _app = faust.App(
        "faust-consumer",
        broker=broker,
        store=store,
        cache=cache,
        topic_partitions=topic_partitions,
        **kwargs,
    )
    return _app


# a default app is created here to be exported
app: AppT = app_builder()

__all__ = ["app", "app_builder"]
