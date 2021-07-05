'''
@Author: Ranjith G C
@Date: 2021-07-05
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-05 
@Title : Program Aim to find common items from two lists. 
'''
from loggers import logger

def common_items():
    '''
    Description:
        This function finds common items from two lists.
    '''
    try:

        list1 = [1,2,3,4,5,6,7]
        list2 = [2,3,5,7]
        list3 = []

        for item in list1:
            if list2.__contains__(item):
                list3.append(item)

        logger.info("Commom Elements are")
        logger.info(list3)
    
    except Exception:
        logger.error("Invalid Input")

common_items()