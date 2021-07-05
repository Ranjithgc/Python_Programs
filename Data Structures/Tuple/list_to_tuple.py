'''
@Author: Ranjith G C
@Date: 2021-07-05
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-05 
@Title : Program Aim to convert list into tuple
'''
from loggers import logger

try:

    list = [1, 2, 3, 4, 5]

    logger.info(list)

    tuple = tuple(list)

    logger.info(tuple)

except Exception:
    logger.info("Invalid")