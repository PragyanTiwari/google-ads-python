
transport inheritance structure
_______________________________

`FeedServiceTransport` is the ABC for all transports.
- public child `FeedServiceGrpcTransport` for sync gRPC transport (defined in `grpc.py`).
- public child `FeedServiceGrpcAsyncIOTransport` for async gRPC transport (defined in `grpc_asyncio.py`).
- private child `_BaseFeedServiceRestTransport` for base REST transport with inner classes `_BaseMETHOD` (defined in `rest_base.py`).
- public child `FeedServiceRestTransport` for sync REST transport with inner classes `METHOD` derived from the parent's corresponding `_BaseMETHOD` classes (defined in `rest.py`).
