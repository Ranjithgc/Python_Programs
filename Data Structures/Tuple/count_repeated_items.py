'''
@Author: Ranjith G C
@Date: 2021-07-05
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-05 
@Title : Program Aim to count repeated items in tuple
'''
from loggers import logger

try:

    #create a tuple
    tuplex = 2, 4, 5, 6, 2, 3, 4, 4, 7
    logger.info(tuplex)
    #return the number of times it appears in the tuple.
    count = tuplex.count(4)
    logger.info(count)

except Exception:
    logger.error("Invalid")