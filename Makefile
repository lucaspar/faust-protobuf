.PHONY: proto

install:
	uv sync --upgrade

proto:
	uv run python -m grpc_tools.protoc -I . --python_out=app proto/greetings.proto

run: proto
	uv run python -m app.app worker
