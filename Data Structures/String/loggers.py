import logging

logger = logging
   
# logging basic config method and saving log files
logger.basicConfig(filename='string.log', level=logging.INFO)
logger.basicConfig(filename='string.log', level=logging.ERROR)