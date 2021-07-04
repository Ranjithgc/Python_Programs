'''
@Author: Ranjith G C
@Date: 2021-07-04
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-04 
@Title : Program Aim to remove items, if it is present in a set
'''

from loggers import logger

def remove_item():
    '''
    Description:
        This function to remove items, if it is present in a set
    '''
    
    try:
        
        #Create a new set
        num_set = set([0, 1, 2, 3, 4, 5])
        logger.info("Original set elements:")
        logger.info(num_set)
        
        logger.info("\nRemove 0 from the said set:")
        num_set.discard(4)
        logger.info(num_set)
        
        logger.info("\nRemove 5 from the said set:")
        num_set.discard(5)
        logger.info(num_set)
        
        logger.info("\nRemove 2 from the said set:")
        num_set.discard(5)
        logger.info(num_set)
        
        logger.info("\nRemove 7 from the said set:")
        num_set.discard(15)
        logger.info(num_set)

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    remove_item()