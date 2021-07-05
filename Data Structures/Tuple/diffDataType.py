'''
@Author: Ranjith G C
@Date: 2021-07-05
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-05 
@Title : Program Aim to Create different data types in tuple 
'''
from loggers import logger

try:

    #Create an tuple with tuple() function built-in Python
    tuple1 = tuple({1, 2.5, 'abc'})
    logger.info(tuple1)

except Exception:
    logger.error("Invalid")