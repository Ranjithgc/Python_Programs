import logging

logger = logging
   
# logging basic config method and saving log files
logger.basicConfig(filename='addressbook.log', level=logging.INFO)
logger.basicConfig(filename='addressbook.log', level=logging.ERROR)