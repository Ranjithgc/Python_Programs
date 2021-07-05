import logging

logger = logging
   
# logging basic config method and saving log files
logger.basicConfig(filename='list.log', level=logging.INFO)
logger.basicConfig(filename='list.log', level=logging.ERROR)