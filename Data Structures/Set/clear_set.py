'''
@Author: Ranjith G C
@Date: 2021-07-04
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-04 
@Title : Program Aim to clear a set 
'''

from loggers import logger

def clear_set():
    '''
    Description:
        This function clears a set
    '''

    try:
        
        setc = {"Red", "Green", "Black", "White"}
        logger.info("Original set elements:")
        logger.info(setc)        
        logger.info("\nAfter removing all elements of the said set.")
        setc.clear()
        logger.info(setc)
    
    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    clear_set()        
