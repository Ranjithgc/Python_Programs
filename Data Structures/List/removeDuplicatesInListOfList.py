'''
@Author: Ranjith G C
@Date: 2021-07-05
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-05 
@Title : Program Aim to remove duplicates from list of list
 
'''

from loggers import logger
import itertools

def remove():
    '''
    Description:
        Removes duplicates from list of list
    '''

    try:
        
        num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
        logger.info("original list")
        logger.info(num)
        
        num.sort()
        
        new_num = list(num for num,_ in itertools.groupby(num))
        logger.info("New list")
        logger.info(new_num)

    except Exception:
        logger.error("Invalid Input")

remove()

        