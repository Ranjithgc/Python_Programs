'''
@Author: Ranjith G C
@Date: 2021-07-05
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-05 
@Title : Program Aim to multiply all the elements in a list.
'''

from loggers import logger

def multiply_list():
    '''
    Description:
        This function implements multiply all the elements
        in a list.
    '''
    try:
        
        items = [1, 2, 3, 4, 5]
        multiply = 1
        for x in items:
            multiply *= x
        
        logger.info(multiply)

    except Exception:
        logger.error("Invalid input")

multiply_list()