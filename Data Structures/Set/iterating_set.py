'''
@Author: Ranjith G C
@Date: 2021-07-04
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-04 
@Title : Program Aim to iterate through a set 
'''

from loggers import logger

def iterating_set():
    '''
    Description:
        This function to iterate through a set
    '''

    try:
        #Create a set 
        num_set = set([0, 1, 2, 3, 4, 5])
        for n in num_set:
            logger.info(n)

        logger.info("\n\nCreating a set using string:")
        char_set = set("Ranjith")  

        # Iterating using for loop
        for val in char_set:
            logger.info(val)

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    iterating_set()