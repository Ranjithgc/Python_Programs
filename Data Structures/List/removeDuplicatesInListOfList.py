'''
@Author: Ranjith G C
@Date: 2021-07-05
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-05 
@Title : Program Aim to remove duplicates from list of list
 
'''

from loggers import logger

def remove():
    '''
    Description:
        Removes duplicates from list of list
    '''

    try:
        list1 = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
        list2 = []

        for value in list1:
            if value not in list2:
                list2.append(value)
        
        logger.info(list2)

    except Exception:
        logger.error("Invalid Input")

remove()

        