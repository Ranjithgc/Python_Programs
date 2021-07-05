'''
@Author: Ranjith G C
@Date: 2021-07-05
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-05 
@Title : Program Aim to reverse a tuple
'''
from loggers import logger

try:

    tuple1 = ("Ranjithgc")

    tuple2 = reversed(tuple1)

    logger.info(tuple(tuple2))

    tupl1 = (5, 10, 15, 20)

    tupl2 = reversed(tupl1)

    logger.info(tuple(tupl2))

except Exception:
    logger.error("Invalid Input")