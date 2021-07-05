'''
@Author: Ranjith G C
@Date: 2021-07-05
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-05 
@Title : Program Aim to check element exists or not
'''
from loggers import logger

try:
    
    tuplex = ('a', 'b', 'c', 'd', 5, 4, 7)
    logger.info("r" in tuplex)
    logger.info(5 in tuplex)

except Exception:
    logger.error("Invalid")