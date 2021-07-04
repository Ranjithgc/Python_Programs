'''
@Author: Ranjith G C
@Date: 2021-07-04
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-04 
@Title : Program Aim to create set difference 
'''

from loggers import logger

def difference():
    '''
    Description:
        This function to create set difference
    '''
    try:

        setc1 = set(["green", "blue"])
        setc2 = set(["blue", "yellow"])
        logger.info("Original sets:")
        logger.info(setc1)
        logger.info(setc2)
        r1 = setc1.difference(setc2)
        logger.info("\nDifference of setc1 - setc2:")
        logger.info(r1)
        r2 = setc2.difference(setc1)
        logger.info("\nDifference of setc2 - setc1:")
        logger.info(r2)
        
        setn1 = set([1, 1, 2, 3, 4, 5])
        setn2 = set([1, 5, 6, 7, 8, 9])
        logger.info("\nOriginal sets:")
        logger.info(setn1)
        logger.info(setn2)
        r1 = setn1.difference(setn2)
        logger.info("\nDifference of setn1 - setn2:")
        logger.info(r1)
        r2 = setn2.difference(setn1)
        logger.info("\nDifference of setn2 - setn1:")
        logger.info(r2)

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    difference()        