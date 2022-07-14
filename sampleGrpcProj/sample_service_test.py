from datetime import datetime, timedelta, timezone
import time
import grpc
import grpc_testing
import unittest
import sample_service_pb2
from sample_service import SampleService
from google.protobuf.timestamp_pb2 import Timestamp
from logger import logger
from faker import Faker

class SampleServiceTest(unittest.TestCase):

	def setUp(self):
		logger.info( f"=== Method: { self._testMethodName } =======" )
		servicers = {
			sample_service_pb2.DESCRIPTOR.services_by_name['SampleService']: SampleService()
		}

		self.test_server = grpc_testing.server_from_dictionary(
			servicers, grpc_testing.strict_real_time())

	def tearDown(self):
		logger.info( f"Method: { self._testMethodName } Done." )
		logger.info( f"---------------------------------------------" )
		logger.info( f"\n" )

	def test_doSimple(self):
		faker = Faker()
		request = sample_service_pb2.Request( input=faker.name() )

		doSimple_method = self.test_server.invoke_unary_unary(
			method_descriptor=(sample_service_pb2.DESCRIPTOR
				.services_by_name['SampleService']
				.methods_by_name['doSimple']),
			invocation_metadata={},
			request=request, timeout=1)

		response, _, code, _ = doSimple_method.termination()
		self.assertEqual( code, grpc.StatusCode.OK )
		self.assertEqual( response.output, f"Hello { request.input }!" )

	def test_doResponseStreaming(self):
		faker = Faker()
		request = sample_service_pb2.Request( input=faker.name() )

		doResponseStreaming_method = self.test_server.invoke_unary_unary(
			method_descriptor=(sample_service_pb2.DESCRIPTOR
				.services_by_name['SampleService']
				.methods_by_name['doResponseStreaming']),
			invocation_metadata={},
			request=request, timeout=1)

		response_generator, _, code, _ = doResponseStreaming_method.termination()
		self.assertEqual( code, grpc.StatusCode.OK )

		for res in response_generator:
			logger.info( f"{res.output=}" )

	def test_doRequestStreaming(self):

		def get_fake_name_generator():
			faker = Faker()
			for _ in range( 10 ):
				time.sleep( 0.5 )
				name = faker.name()
				logger.info( f"Send request with { name }." )
				yield sample_service_pb2.Request( input=name )

		request = get_fake_name_generator()
		doRequestStreaming_method = self.test_server.invoke_unary_unary(
			method_descriptor=(sample_service_pb2.DESCRIPTOR
				.services_by_name['SampleService']
				.methods_by_name['doRequestStreaming']),
			invocation_metadata={},
			request=request, timeout=10)

		response, _, code, _ = doRequestStreaming_method.termination()
		self.assertEqual( code, grpc.StatusCode.OK )
		logger.info( f"{ response.output= }" )

	@unittest.skip
	def test_doBidirectional(self):

		def get_fake_name_generator():
			faker = Faker()
			for _ in range( 10 ):
				time.sleep( 0.5 )
				name = faker.name()
				logger.info( f"Send request with { name }." )
				yield sample_service_pb2.Request( input=name )

		request = get_fake_name_generator()
		doBidirectional_method = self.test_server.invoke_unary_unary(
			method_descriptor=(sample_service_pb2.DESCRIPTOR
				.services_by_name['SampleService']
				.methods_by_name['doBidirectional']),
			invocation_metadata={},
			request=request, timeout=10)

		response_generator, _, code, _ = doBidirectional_method.termination()
		self.assertEqual( code, grpc.StatusCode.OK )
		for res in response_generator:
			logger.info( f"{ res.output= }" )

	def test_doSpecialDataType( self ):
		faker = Faker()
		KST = timezone( timedelta( hours=9 ) )
		current_datetime = datetime.now().replace( tzinfo=KST )
		timestamp = Timestamp()
		timestamp.FromDatetime( current_datetime )
		names = [ faker.name() for i in range( 10 )]
		name2phoneNumMap = { name: faker.phone_number() for name in names }
		cardInfos = [ sample_service_pb2.CardInfo( name=faker.name(), numberOfCreditCard=1 ) for i in range( 10 ) ]

		logger.info( f"request.date={ datetime.strftime( current_datetime, '%Y-%m-%d %H:%M:%S%Z' ) }" )
		logger.info( f"request.names={ names }" )
		logger.info( f"request.name2phoneNumMap={ name2phoneNumMap }" )
		logger.info( f"request.cardInfos={ cardInfos }" )
		request = sample_service_pb2.SpecialDataTypeRequest(
			date=timestamp,
			names=names,
			name2phoneNumMap=name2phoneNumMap,
			cardInfos=cardInfos,
		)

		doSpecialDataType_method = self.test_server.invoke_unary_unary(
			method_descriptor=(sample_service_pb2.DESCRIPTOR
				.services_by_name['SampleService']
				.methods_by_name['doSpecialDataType']),
			invocation_metadata={},
			request=request, timeout=1)

		response, _, code, _ = doSpecialDataType_method.termination()
		self.assertEqual( code, grpc.StatusCode.OK )

		result_date = datetime.fromtimestamp(response.date.seconds + response.date.nanos/1e9)
		logger.info( f"result_date={ datetime.strftime( result_date.replace( tzinfo=KST ), '%Y-%m-%d %H:%M:%S%Z' ) }" )
		logger.info( f"{ response.names= }")
		logger.info( f"{ response.name2phoneNumMap= }")
		logger.info( f"{ response.cardInfos= }")


if __name__ == '__main__':
	unittest.main()