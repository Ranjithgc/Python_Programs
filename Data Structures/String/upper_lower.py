'''
@Author: Ranjith G C
@Date: 2021-07-06
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-06 
@Title : Program Aim converts a string to lower and upper case
'''
from loggers import logger

try:
    
    string = input("Enter the String")

    logger.info(string.upper())
    logger.info(string.lower())

except Exception:
    logger.error("Invalid Input")

