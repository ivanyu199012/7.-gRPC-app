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
		""" expect to get Cases response """
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
		""" expect to get Cases response """
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

		logger.info( f"{ response_generator= }")
		for res in response_generator:
			logger.info( f"{res.output=}" )

if __name__ == '__main__':
	unittest.main()