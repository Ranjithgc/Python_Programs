'''
@Author: Ranjith G C
@Date: 2021-07-05
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-05 
@Title : Program Aim to minimum number in a list.
'''

from loggers import logger

def minimum_list():
    '''
    Description:
        This function finds minimum number
        in a list.
    '''
    try:
        
        items = [5, 4, 3, 8, 1]
        min = items[0]
        
        for x in range(len(items)):
            if items[x] < min:
                min = items[x]
        
        logger.info(min)
        
    except Exception:
        logger.error("Invalid input")

def min_list():
    '''
    Description:
        This function first sorts the list and access the 
        first index value.
    '''
    try:

        number = [5, 20, 18, 2, 15]

        number.sort()

        logger.info(number[0])
    
    except Exception:
        logger.error("Invalid Input")

minimum_list()
min_list()