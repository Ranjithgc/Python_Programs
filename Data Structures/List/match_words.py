'''
@Author: Ranjith G C
@Date: 2021-07-05
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-05 
@Title : Program Aim Count the number of strings where the 
        string length is 2 or more and the first and last 
        character are same from a given list of strings.
'''

from loggers import logger

def compare(list):
    '''
    Description:
        This function counts the number of string where
        the string length is 2 or more and the first and
        last character are same.
    Parameter:

    '''
    ctr = 0
    for i in list:
        if len(i) > 2 and i[0] == i[-1]:
            ctr+= 1
    return ctr

list = ['abc', 'xyz', 'aba', 'bcd', 'def']
logger.info(compare(list))
