'''
@Author: Ranjith G C
@Date: 2021-07-06
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-06 
@Title : Program Aim to prints the last part of a string before a specified character
'''
from loggers import logger

try:

    str1 = 'https://www.w3resource.com/python-exercises/string'
    logger.info(str1.rsplit('/', 1)[0])
    logger.info(str1.rsplit('-', 1)[0])


except Exception:
    logger.error("Invalid input")