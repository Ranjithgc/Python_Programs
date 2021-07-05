'''
@Author: Ranjith G C
@Date: 2021-07-05
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-05 
@Title : Program Aim to remove duplicate elements in list
'''

from loggers import logger

def remove_duplicates():
    '''
    Description:
        This function removes duplicate elements in list
    '''

    try:
        list = [1,2,3,2,1,5,6,4,8,5,4]

        dup_items = set()
        
        for x in list:
            if x not in dup_items:
                dup_items.add(x)

        logger.info(dup_items)

    except Exception:
        logger.error("Invalid Input")

remove_duplicates()

