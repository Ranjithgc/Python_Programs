'''
@Author: Ranjith G C
@Date: 2021-07-04
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-04 
@Title : Program Aim to find maximum and minimum value in a set
'''

from loggers import logger

def max_min():
    '''
    Description:
        This function finds maximum and minimum value in a set
    '''
    try:

        #Create a set
        setn = {5, 10, 3, 15, 2, 20}
        logger.info("Original set elements:")
        logger.info(setn)
        logger.info(type(setn))
        logger.info("\nMaximum value of the said set:")
        logger.info(max(setn))
        logger.info("\nMinimum value of the said set:")
        logger.info(min(setn))

    except Exception:
        logger.error("Invalid Input")

if __name__ == "__main__":
    max_min()
