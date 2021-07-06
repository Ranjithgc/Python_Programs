'''
@Author: Ranjith G C
@Date: 2021-07-06
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-06 
@Title : Program Aim to take a list of words and returns the length of the longest one
'''
from loggers import logger

def find_longest_word(words_list):
    '''
    Description:
        This function takes a list of words and
        return the length of the longest one.
    Parameter:
        takes words_list as parameter.
    Return:
        returns the length of the string.
    '''
    
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]

result = find_longest_word(["PHP", "Exercises", "Backend"])
logger.info("Longest word: ")
logger.info(result[1])

logger.info("Length of the longest word: ")
logger.info(result[0])
