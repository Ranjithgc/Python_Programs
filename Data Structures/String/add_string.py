'''
@Author: Ranjith G C
@Date: 2021-07-06
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-06 
@Title : Program Aim to Add 'ing' at the end of a given string 
        (length should be at least 3). If the given string already 
        ends with 'ing' then add 'ly' instead. If the string length 
        of the given string is less than 3, leave it unchanged
'''
from loggers import logger

def add_string(str):
    '''
    Description:
        This function Add 'ing' at the end of a given string 
        (length should be at least 3). If the given string already 
        ends with 'ing' then add 'ly' instead. If the string length 
        of the given string is less than 3, leave it unchanged.
    Parameter:
        function takes str as parameter
    Returns:
        function returns str
    '''

    length = len(str)

    if length > 2:
        if str[-3:] == 'ing':
            str += 'ly'
        else:
            str += 'ing'
    return str

try:

    logger.info(add_string('collection'))
    logger.info(add_string('add'))
    logger.info(add_string('string'))

except Exception:
        logger.error("Invalid Input")
