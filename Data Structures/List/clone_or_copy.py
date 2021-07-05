'''
@Author: Ranjith G C
@Date: 2021-07-05
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-05 
@Title : Program Aim to clone or copy a list
'''

from loggers import logger

def clone_copy():
    '''
    Description:
        This function clone or copy a list
    '''
    try:

        original_list = [10, 22, 44, 23, 4]
        new_list = list(original_list)
        
        logger.info(original_list)
        
        logger.info(new_list)

    except Exception:
        logger.error("invalid Input")

clone_copy()