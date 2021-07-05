'''
@Author: Ranjith G C
@Date: 2021-07-05
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-05 
@Title : Program Aim to slicing of tuple
'''
from loggers import logger

try:

    tuple = (1, 2, 3, 4, 5, 6, 7, 8)

    logger.info(tuple[1:]) # slicing starts from 1 to end

    logger.info(tuple[:5]) # slicing starts from 0 and ends at 5th index
    
    logger.info(tuple[1:4]) # slicing from 1 to 4 

    logger.info(tuple[::2]) # slicing from start to end using step sizes of 2

except Exception:
    logger.error("Invalid input")