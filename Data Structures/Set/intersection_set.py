'''
@Author: Ranjith G C
@Date: 2021-07-04
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-04 
@Title : Program Aim to create interscetion of two sets 
'''

from loggers import logger

def intersection():
    '''
    Description:
        This function to create intersection of sets
    '''
    try:
        
        setx = set(["green", "blue"])
        sety = set(["blue", "yellow"])
        logger.info("Original set elements:")
        logger.info(setx)
        logger.info(sety)
        
        logger.info("\nIntersection of two said sets:")
        setz = setx & sety
        logger.info(setz)
    
    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    intersection()