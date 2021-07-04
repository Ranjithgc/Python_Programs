'''
@Author: Ranjith G C
@Date: 2021-07-04
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-04 
@Title : Program Aim to create union of two sets 
'''

from loggers import logger

def union():
    '''
    Description:
        This function to create union of 2 sets
    '''
    try:

        setc1 = set(["green", "blue"])
        setc2 = set(["blue", "yellow"])
        logger.info("Original sets:")
        logger.info(setc1)
        logger.info(setc2)
        
        setc = setc1.union(setc2)
        logger.info("\nUnion of above sets:")
        logger.info(setc)
        
        setn1 = set([1, 1, 2, 3, 4, 5])
        setn2 = set([1, 5, 6, 7, 8, 9])
        logger.info("\nOriginal sets:")
        logger.info(setn1)
        logger.info(setn2)
        
        logger.info("\nUnion of above sets:")
        setn = setn1.union(setn2)
        logger.info(setn)

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    union()
