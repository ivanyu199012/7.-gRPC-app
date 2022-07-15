
from datetime import datetime, timedelta, timezone
import time
from faker import Faker
from google.protobuf.timestamp_pb2 import Timestamp
import grpc
from sample_service_pb2 import Request, CardInfo, SpecialDataTypeRequest
from sample_service_pb2_grpc import SampleServiceStub
from logger import logger

class SampleClient:

	faker = Faker()

	@classmethod
	def call_doSimple( self ):
		with grpc.insecure_channel('localhost:50051') as channel:
			stub = SampleServiceStub( channel )
			request = Request( input=self.faker.name() )
			logger.info( f"doSimple client sent: { request.input }" )
			response = stub.doSimple( request )
			logger.info( f"doSimple client received: { response.output }" )

	@classmethod
	def call_doResponseStreaming( self ):
		with grpc.insecure_channel('localhost:50051') as channel:
			stub = SampleServiceStub( channel )
			request = Request( input=self.faker.name() )
			logger.info( f"doResponseStreaming client sent: { request.input }" )
			response_generator = stub.doResponseStreaming( request )
			for response in response_generator:
				logger.info( f"doResponseStreaming client received: { response.output }" )

	@classmethod
	def call_doRequestStreaming( self ):

		def get_fake_name_generator():
			faker = Faker()
			for _ in range( 3 ):
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
			for _ in range( 3 ):
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
	def call_doSpecialDataType( self ):

		KST = timezone( timedelta( hours=9 ) )
		current_datetime = datetime.now().replace( tzinfo=KST )
		timestamp = Timestamp()
		timestamp.FromDatetime( current_datetime )
		names = [ self.faker.name() for i in range( 3 )]
		name2phoneNumMap = { name: self.faker.phone_number() for name in names }
		cardInfos = [ CardInfo( name=self.faker.name(), numberOfCreditCard=1 ) for i in range( 3 ) ]

		logger.info( f"doSpecialDataType client sent: request.date={ datetime.strftime( current_datetime, '%Y-%m-%d %H:%M:%S%Z' ) }" )
		logger.info( f"doSpecialDataType client sent: request.names={ names }" )
		logger.info( f"doSpecialDataType client sent: request.name2phoneNumMap={ name2phoneNumMap }" )
		logger.info( f"doSpecialDataType client sent: request.cardInfos={ cardInfos }" )

		with grpc.insecure_channel('localhost:50051') as channel:
			stub = SampleServiceStub( channel )
			request = SpecialDataTypeRequest(
				date=timestamp,
				names=names,
				name2phoneNumMap=name2phoneNumMap,
				cardInfos=cardInfos,
			)
			response = stub.doSpecialDataType( request )
			result_date = datetime.fromtimestamp(response.date.seconds + response.date.nanos/1e9)
			logger.info( f"doSpecialDataType client received: request.date={ datetime.strftime( result_date.replace( tzinfo=KST ), '%Y-%m-%d %H:%M:%S%Z' ) }" )
			logger.info( f"doSpecialDataType client received: { response.names= }" )
			logger.info( f"doSpecialDataType client received: { response.name2phoneNumMap= }" )
			logger.info( f"doSpecialDataType client received: { response.cardInfos= }" )

	@classmethod
	def run( self ):
		self.call_doSimple()
		self.call_doResponseStreaming()
		self.call_doRequestStreaming()
		self.call_doBidirectional()
		self.call_doSpecialDataType()

if __name__ == '__main__':
	SampleClient.run()