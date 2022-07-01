# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import sample_service_pb2 as sample__service__pb2


class SampleServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.doSimple = channel.unary_unary(
                '/SampleService/doSimple',
                request_serializer=sample__service__pb2.Request.SerializeToString,
                response_deserializer=sample__service__pb2.Response.FromString,
                )
        self.doResponseStreaming = channel.unary_stream(
                '/SampleService/doResponseStreaming',
                request_serializer=sample__service__pb2.Request.SerializeToString,
                response_deserializer=sample__service__pb2.Response.FromString,
                )
        self.doRequestStreaming = channel.stream_unary(
                '/SampleService/doRequestStreaming',
                request_serializer=sample__service__pb2.Request.SerializeToString,
                response_deserializer=sample__service__pb2.Response.FromString,
                )
        self.doBidirectional = channel.stream_stream(
                '/SampleService/doBidirectional',
                request_serializer=sample__service__pb2.Request.SerializeToString,
                response_deserializer=sample__service__pb2.Response.FromString,
                )
        self.doSpecialDataType = channel.unary_unary(
                '/SampleService/doSpecialDataType',
                request_serializer=sample__service__pb2.SpecialDataTypeRequest.SerializeToString,
                response_deserializer=sample__service__pb2.SpecialDataTypeResponse.FromString,
                )


class SampleServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def doSimple(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def doResponseStreaming(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def doRequestStreaming(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def doBidirectional(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def doSpecialDataType(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SampleServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'doSimple': grpc.unary_unary_rpc_method_handler(
                    servicer.doSimple,
                    request_deserializer=sample__service__pb2.Request.FromString,
                    response_serializer=sample__service__pb2.Response.SerializeToString,
            ),
            'doResponseStreaming': grpc.unary_stream_rpc_method_handler(
                    servicer.doResponseStreaming,
                    request_deserializer=sample__service__pb2.Request.FromString,
                    response_serializer=sample__service__pb2.Response.SerializeToString,
            ),
            'doRequestStreaming': grpc.stream_unary_rpc_method_handler(
                    servicer.doRequestStreaming,
                    request_deserializer=sample__service__pb2.Request.FromString,
                    response_serializer=sample__service__pb2.Response.SerializeToString,
            ),
            'doBidirectional': grpc.stream_stream_rpc_method_handler(
                    servicer.doBidirectional,
                    request_deserializer=sample__service__pb2.Request.FromString,
                    response_serializer=sample__service__pb2.Response.SerializeToString,
            ),
            'doSpecialDataType': grpc.unary_unary_rpc_method_handler(
                    servicer.doSpecialDataType,
                    request_deserializer=sample__service__pb2.SpecialDataTypeRequest.FromString,
                    response_serializer=sample__service__pb2.SpecialDataTypeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SampleService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SampleService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def doSimple(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SampleService/doSimple',
            sample__service__pb2.Request.SerializeToString,
            sample__service__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def doResponseStreaming(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/SampleService/doResponseStreaming',
            sample__service__pb2.Request.SerializeToString,
            sample__service__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def doRequestStreaming(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/SampleService/doRequestStreaming',
            sample__service__pb2.Request.SerializeToString,
            sample__service__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def doBidirectional(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/SampleService/doBidirectional',
            sample__service__pb2.Request.SerializeToString,
            sample__service__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def doSpecialDataType(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SampleService/doSpecialDataType',
            sample__service__pb2.SpecialDataTypeRequest.SerializeToString,
            sample__service__pb2.SpecialDataTypeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)