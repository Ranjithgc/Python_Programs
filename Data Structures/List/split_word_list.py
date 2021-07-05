'''
@Author: Ranjith G C
@Date: 2021-07-05
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-05 
@Title : Program Aim to Split a list based on first character of word
 
'''

from loggers import logger

def split():
    '''
    Description:
         This function Splits a list based on first character of word
    '''
    try:
        
        list1 = ['Split', 'list', 'based', 'on', 'first', 'character', 'word']
        # creating the list of just the first character in each item of the list
        list2 = [item[0] for item in list1]
        logger.info(list2)

    except Exception as e:
        logger.error(e)

split()