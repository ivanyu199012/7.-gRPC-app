from concurrent import futures
from datetime import datetime, timedelta, timezone
import time
from faker import Faker
from google.protobuf.timestamp_pb2 import Timestamp
import grpc
import pytz
from logger import logger

from sample_service_pb2 import Response, SpecialDataTypeResponse, CardInfo
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
			time.sleep( 0.5 )
			yield Response( output=name )

	def doRequestStreaming(self, request_iterator, context):
		result_list = []
		for request in request_iterator:
			result_list.append( request.input.upper() )
			logger.info( f"{ request.input.upper() } is appended to the list" )

		return Response( output=",".join( result_list ) )


	def doBidirectional(self, request_iterator, context):
		for request in request_iterator:
			yield Response( output=request.input + " is excellent!" )

	def doSpecialDataType(self, request, context):

		KST = timezone( timedelta( hours=9 ) )
		dateWithTime = datetime.fromtimestamp(request.date.seconds + request.date.nanos/1e9).replace( tzinfo=KST ) + timedelta(hours=1)
		added_name = "Boris Lee"
		names = [ *request.names, added_name ]
		name2phoneNumMap = { **request.name2phoneNumMap, added_name : "02-1577-8688" }
		cardInfos = request.cardInfos
		cardInfos.append( CardInfo( name="Boris Lee", numberOfCreditCard=0 ) )

		timestamp = Timestamp()
		timestamp.FromDatetime( dateWithTime )
		return SpecialDataTypeResponse(
			date=timestamp,
			names=names,
			name2phoneNumMap=name2phoneNumMap,
			cardInfos=cardInfos,
		)

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
