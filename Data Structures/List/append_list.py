'''
@Author: Ranjith G C
@Date: 2021-07-05
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-05 
@Title : Program Aim to Append a list to the second list 
'''
from loggers import logger

try:

    list1 = [1, 2, 3, 0]
    list2 = ['abc', 'def', 'ghi']
    final_list = list1 + list2
    logger.info(final_list)

except Exception:
    logger.error("Invalid Input")