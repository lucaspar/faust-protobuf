# faust-protobuf

An example how use [`faust-streaming`](https://github.com/faust-streaming/faust) a python based stream processing library with `protobuf`

## Run Instructions

Run a Kafka broker and Zookeeper using docker compose.

```bash
docker compose up -d
docker compose logs -f
```

On another terminal, run the producers and consumers:

```bash
poetry install --no-root
poetry run python -m grpc_tools.protoc -I . \
    --python_out=app \
    --mypy_out=app \
    proto/greetings.proto
poetry run python -m app.app worker
```
