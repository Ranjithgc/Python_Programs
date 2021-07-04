import logging

logger = logging
   
# logging basic config method and saving log files
logger.basicConfig(filename='dictinary.log', level=logging.INFO)
logger.basicConfig(filename='dictionary.log', level=logging.ERROR)