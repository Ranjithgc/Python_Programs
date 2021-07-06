'''
@Author: Ranjith G C
@Date: 2021-07-06
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-06 
@Title : Program Aim to reverse a string
'''
from loggers import logger

def reverse():
    '''
    Description:
        This function reverses a string
    '''
    try:
    
        s = "Ranjithgc"
        string = s[::-1]
        logger.info("Reversed String is")  
        logger.info(string)
    
    except Exception:
        logger.error("Invalid Input") 

reverse()