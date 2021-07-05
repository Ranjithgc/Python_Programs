'''
@Author: Ranjith G C
@Date: 2021-07-05
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-05 
@Title : Program Aim to find Difference between the two lists
'''
from loggers import logger

try:

    list1 = [1, 3, 5, 7, 9]
    list2=[1, 2, 4, 6, 7, 8]
    diff_list1_list2 = list(set(list1) - set(list2))
    diff_list2_list1 = list(set(list2) - set(list1))
    total_diff = diff_list1_list2 + diff_list2_list1
    logger.info(total_diff)

except Exception:
    logger.error("Invalid Input")