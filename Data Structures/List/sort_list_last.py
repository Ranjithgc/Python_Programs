'''
@Author: Ranjith G C
@Date: 2021-07-05
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-05 
@Title : Program Aim to minimum number in a list.
'''

from loggers import logger

def last(num):
    '''
    Description:
        This function returns the last tuple items in the list
    Parameter:
        it takes num as parameter.
    Return:
        it returns the num
    ''' 
    return num[-1]

def sort_list_last(tuples):
    '''
    Description:
        This function returns the sorted tuple to the called function
    Parameter:
        it takes tuples as parameter
    Return:
        it return the sorted last tuple items.
    '''
    
    return sorted(tuples, key=last)

logger.info(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))