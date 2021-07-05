'''
@Author: Ranjith G C
@Date: 2021-07-05
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-05 
@Title : Program Aim to Print a list after removing specified elements
'''

from loggers import logger

def remove_specified():
    '''
    Description:
        to print a list after removing specified elements
    '''
    try:
        state = ['karnataka', 'Gujarat', 'Westbengal', 'Punjab', 'UP', 'Telangana']
        state1 = [x for (i,x) in enumerate(state) if i not in (0,4,5)]
        logger.info(state1)
    except Exception:
        logger.error("Invalid Input")

remove_specified()