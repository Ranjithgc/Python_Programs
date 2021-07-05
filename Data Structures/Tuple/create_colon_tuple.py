'''
@Author: Ranjith G C
@Date: 2021-07-05
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-05 
@Title : Program Aim to create a colon tuple
'''
from loggers import logger
from copy import deepcopy

try:

    #Create an tuple with tuple() function built-in Python
    tuple1 = tuple({1, 2.5, 3, 4})

    tuple2 = deepcopy(tuple1)
    tuple2[2].append(5)
    logger.info(tuple2)

except Exception:
    logger.error("Invalid")