'''
@Author: Ranjith G C
@Date: 2021-07-04
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-04 
@Title : Program Aim to sum of all the elements in a list.
'''

from loggers import logger

def sum_list():
    '''
    Description:
        This function implements sum of all the elements
        in a list.
    '''
    try:
        
        items = [1, 2, 3, 4, 5]
        sum_numbers = 0
        for x in items:
            sum_numbers += x
        
        logger.info(sum_numbers)

    except Exception:
        logger.error("Invalid input")

sum_list()