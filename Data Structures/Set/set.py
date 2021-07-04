'''
@Author: Ranjith G C
@Date: 2021-07-04
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-04 
@Title : Program Aim to create a set
'''

from logging import log
from loggers import logger

def create_set():
    '''
    Description:
        This function creates a set.
    '''
    try:
        
        logger.info("Create a new set:")
        x = set()
        logger.info(x)
        logger.info(type(x))

        logger.info("\nCreate a non empty set:")
        n = set([0, 1, 2, 3, 4])
        logger.info(n)
        logger.info(type(n))
    
        logger.info("\nUsing a literal:")
        a = {1,2,3,'foo','bar'}
        logger.info(type(a))
        logger.info(a)

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    create_set()