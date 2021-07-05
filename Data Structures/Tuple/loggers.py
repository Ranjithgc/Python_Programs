import logging

logger = logging
   
# logging basic config method and saving log files
logger.basicConfig(filename='tuple.log', level=logging.INFO)
logger.basicConfig(filename='tuple.log', level=logging.ERROR)