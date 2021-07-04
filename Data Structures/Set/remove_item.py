'''
@Author: Ranjith G C
@Date: 2021-07-04
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-04 
@Title : Program Aim to remove items from a set
'''

from loggers import logger

def remove_item():
    '''
    Description:
        This function to remove items from a set
    '''

    try:
        num_set = set([0, 1, 3, 4, 5])
        logger.info("Original set:")
        logger.info(num_set)
        
        num_set.pop()
        logger.info("\nAfter removing the first element from the said set:")
        logger.info(num_set)


    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    remove_item()
