'''
@Author: Ranjith G C
@Date: 2021-07-04
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-04 
@Title : Program Aim to count number of items in a dictionary value that is a list.
'''

from loggers import logger

def count_number_items():
    '''
    Description:
        to count number of items in a dictionary value that is a list.
    '''
    
    dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
    ctr = sum(map(len, dict.values()))
    
    logger.info(ctr)

if __name__ == "__main__":
    count_number_items()