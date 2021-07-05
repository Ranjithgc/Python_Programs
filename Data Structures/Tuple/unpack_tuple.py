'''
@Author: Ranjith G C
@Date: 2021-07-05
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-05 
@Title : Program Aim to unpack a tuple in several variables
'''
from loggers import logger

try:

    #Create an tuple with tuple() function built-in Python
    tuple1 = tuple({1, 2.5, 'abc'})
    
    #unpacking tuple into several variables
    t1, t2, t3 = tuple1

    logger.info(t1)
    logger.info(t2)
    logger.info(t3)

except Exception:
    logger.error("Invalid")