'''
@Author: Ranjith G C
@Date: 2021-07-06
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-06 
@Title : Program Aim to Get a string from a given string where all 
         occurrences of its first char have been changed to '$'
'''
from loggers import logger

def change_char():
    '''
    Description:
        Get a string from a given string where all occurrences 
        of its first char have been changed to '$'
    '''
    try:
        
        str = "restart"
        char = str[0]
        
        logger.info("Before Replacing")
        logger.info(str)
        
        str1 = str.replace(char, '$')
        str1 = char + str1[1:]

        logger.info("After Replacing")
        logger.info(str1)

    except Exception:
        logger.error("Invalid input")

change_char()