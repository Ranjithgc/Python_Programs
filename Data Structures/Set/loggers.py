import logging

logger = logging
   
# logging basic config method and saving log files
logger.basicConfig(filename='set.log', level=logging.INFO)
logger.basicConfig(filename='set.log', level=logging.ERROR)