'''
@Author: Ranjith G C
@Date: 2021-07-06
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-06 
@Title : Program Aim to Count the number of characters (character frequency) in a string
'''
from loggers import logger

def char_frequency(str1):
    '''
    Description:
        Count the number of characters (character frequency) in a string
    Parameter:
        str1 is parameter.
    Return:
        returns dict - count of characters
    '''
    try:
        dict = {}
        for n in str1:
            keys = dict.keys()
            if n in keys:
                dict[n] += 1
            else:
                dict[n] = 1
        return dict

    except Exception:
        logger.error("Invalid")
        
logger.info(char_frequency('Ranjithgc'))
