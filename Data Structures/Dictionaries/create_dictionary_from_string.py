'''
@Author: Ranjith G C
@Date: 2021-07-04
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-04 
@Title : Program Aim to create a dictionary from string
'''

from loggers import logger
from collections import defaultdict, Counter

def create():
    '''
    Description:
        This function to create a dictionary from a string
    '''
    
    try:
        str1 = 'w3resource' 
        my_dict = {}
        
        for letter in str1:
            my_dict[letter] = my_dict.get(letter, 0) + 1
        
        logger.info(my_dict)

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    create()