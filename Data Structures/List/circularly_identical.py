'''
@Author: Ranjith G C
@Date: 2021-07-05
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-05 
@Title : Program Aim to check whether two lists are circularly identical 
'''
from loggers import logger

try:

    list1 = [10, 10, 0, 0, 10]
    list2 = [10, 10, 10, 0, 0]
    list3 = [1, 10, 10, 0, 0]

    logger.info('Compare list1 and list2')
    logger.info(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))   
    
    logger.info('Compare list1 and list3')
    logger.info(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))

except Exception:
    logger.error("Invalid Input")