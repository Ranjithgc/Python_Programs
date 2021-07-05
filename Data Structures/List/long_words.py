'''
@Author: Ranjith G C
@Date: 2021-07-05
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-05 
@Title : Program Aim Find the list of words that are 
        longer than n from a given list of words
'''

from loggers import logger

def long_words():
    '''
    Description:
        This function Find the list of words that are longer
        than n from a given list of words
    '''
    try:

        str = "Find the list of words that are longer than n from a given list of words"
        n = int(input("Enter the length"))
        word_len = []
        txt = str.split(" ")
        
        for x in txt:
            if len(x) > n:
                word_len.append(x)
        
        logger.info(word_len)
    
    except Exception:
        logger.error("Invalid input")

long_words()