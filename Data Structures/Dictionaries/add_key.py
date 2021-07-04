'''
@Author: Ranjith G C
@Date: 2021-07-04
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-04 
@Title : Program Aim to add a key to dictionary
'''

from loggers import logger
def add_key():
    '''
    Description:
        This function adds the key to dictionary
    '''
    try:
        dict = {
                0: 10,
                1: 20,
               }

        print(dict)

        dict.update({2: 30})

        logger.info(dict)

    except Exception:
        logger.error("Invalid Input")

if __name__ == "__main__":
    add_key()