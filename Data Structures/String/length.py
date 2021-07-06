'''
@Author: Ranjith G C
@Date: 2021-07-06
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-06 
@Title : Program Aim to check the length of a string
'''
from loggers import logger

def length():
    '''
    Description:
        This function finds the length of a string.
    '''

    try:
        
        string = "RanjithGc"
        count = 0
        for char in string:
            count += 1

        logger.info("Length of a String")
        logger.info(count)

    except Exception:
        logger.error("Invalid Input")

length()