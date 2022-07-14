
import time
from faker import Faker
import grpc
from sample_service_pb2 import Request
from sample_service_pb2_grpc import SampleServiceStub
from logger import logger

class SampleClient:

	faker = Faker()

	@classmethod
	def call_doSimple( self ):
		with grpc.insecure_channel('localhost:50051') as channel:
			stub = SampleServiceStub( channel )
			request = Request( input=self.faker.name() )
			response = stub.doSimple( request )
			logger.info( f"doSimple client sent: { request.input }" )
			logger.info( f"doSimple client received: { response.output }" )

	@classmethod
	def call_doResponseStreaming( self ):
		with grpc.insecure_channel('localhost:50051') as channel:
			stub = SampleServiceStub( channel )
			request = Request( input=self.faker.name() )
			response_generator = stub.doResponseStreaming( request )
			logger.info( f"doResponseStreaming client sent: { request.input }" )
			for response in response_generator:
				logger.info( f"doResponseStreaming client received: { response.output }" )

	@classmethod
	def call_doRequestStreaming( self ):

		def get_fake_name_generator():
			faker = Faker()
			for _ in range( 10 ):
				time.sleep( 0.5 )
				name = faker.name()
				logger.info( f"doRequestStreaming client sent: { name }." )
				yield Request( input=name )

		with grpc.insecure_channel('localhost:50051') as channel:
			stub = SampleServiceStub( channel )
			request = get_fake_name_generator()
			response = stub.doRequestStreaming( request )
			logger.info( f"doRequestStreaming client received: { response.output }" )

	@classmethod
	def call_doBidirectional( self ):

		def get_fake_name_generator():
			faker = Faker()
			for _ in range( 10 ):
				time.sleep( 0.5 )
				name = faker.name()
				logger.info( f"doRequestStreaming client sent: { name }." )
				yield Request( input=name )

		with grpc.insecure_channel('localhost:50051') as channel:
			stub = SampleServiceStub( channel )
			request = get_fake_name_generator()
			response_generator = stub.doBidirectional( request )
			for response in response_generator:
				logger.info( f"doBidirectional client received: { response.output }" )

	@classmethod
	def run( self ):
		self.call_doSimple()
		self.call_doResponseStreaming()
		self.call_doRequestStreaming()
		self.call_doBidirectional()

if __name__ == '__main__':
	SampleClient.run()