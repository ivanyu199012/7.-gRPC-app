from concurrent import futures
import time
from faker import Faker
from google.protobuf.timestamp_pb2 import Timestamp

import grpc
from logger import logger

from sample_service_pb2 import Response
from sample_service_pb2_grpc import SampleServiceServicer, add_SampleServiceServicer_to_server

class SampleService( SampleServiceServicer ):

	def doSimple(self, request, context):
		logger.info( f"{ request.input= }" )
		output = f"Hello { request.input }!"
		logger.info( f"{ output= }" )
		return Response( output=f"Hello { request.input }!" )

	def doResponseStreaming(self, request, context):
		logger.info( f"{ request.input= }" )
		faker = Faker()
		name_list = [ faker.name() for i in range( 10 ) ]
		name_list.append( request.input )
		logger.info( f"{ name_list= }" )

		for name in name_list:
			time.sleep( 1 )
			yield Response( output=name )

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

	@classmethod
	def serve( self ):
		port = 50051
		server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
		add_SampleServiceServicer_to_server( SampleService(), server)
		server.add_insecure_port(f'[::]:{ port }')
		server.start()
		server.wait_for_termination()


if __name__ == '__main__':
	SampleService.serve()
