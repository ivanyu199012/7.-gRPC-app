#
from datetime import datetime
from enum import Enum
import logging
from logging.handlers import TimedRotatingFileHandler
import os

class CustomLogger:

	__logger = None

	def __new__(self,):
		if not hasattr(self, 'instance'):
			self.instance = super( CustomLogger, self ).__new__(self)

			LOG_FOLDER_NAME = 'log'

			self.__create_folder_if_not_exist( LOG_FOLDER_NAME )

			logFormatter = logging.Formatter( '[ %(asctime)s ][ %(levelname)s ][ %(funcName)s ] %(message)s' )
			self.instance.__logger = logging.getLogger()

			today_date_str = datetime.now().strftime( "%Y-%m-%d" )
			fileHandler = TimedRotatingFileHandler( f'{ LOG_FOLDER_NAME }/{ today_date_str }.log', when='D', interval=1, backupCount=14, encoding='utf-8' )
			fileHandler.setFormatter( logFormatter )
			self.instance.__logger.addHandler( fileHandler )

			consoleHandler = logging.StreamHandler()
			consoleHandler.setFormatter( logFormatter )
			self.instance.__logger.addHandler( consoleHandler )
			self.instance.__logger.setLevel( logging.INFO )
			self.instance.__logger.propagate = False

		return self.instance

	@classmethod
	def get_logger( self ):
		return self().__logger

	@classmethod
	def __create_folder_if_not_exist(self, path):
		if not os.path.exists( path ):
			os.makedirs( path )

logger = CustomLogger().get_logger()
