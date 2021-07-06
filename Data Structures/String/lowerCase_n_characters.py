'''
@Author: Ranjith G C
@Date: 2021-07-06
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-06 
@Title : Program Aim Lowercase first n characters in a string
'''

from loggers import logger

try:

    str1 = 'KARNATAKA'
    logger.info(str1[:4].lower() + str1[4:])

except Exception:
    logger.error("Invalid Input")