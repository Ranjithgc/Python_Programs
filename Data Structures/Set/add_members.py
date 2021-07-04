'''
@Author: Ranjith G C
@Date: 2021-07-04
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-04 
@Title : Program Aim to Add members to a set
'''

from loggers import logger

def add_member():
    '''
    Description:
        This function to Add members to a set
    '''
    try:

        #A new empty set
        color_set = set()
        logger.info(color_set)
        
        logger.info("\nAdd single element:")
        color_set.add("Red")
        logger.info(color_set)
        
        logger.info("\nAdd multiple items:")
        color_set.update(["Blue", "Green"])
        logger.info(color_set)

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    add_member()