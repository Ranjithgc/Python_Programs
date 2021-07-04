'''
@Author: Ranjith G C
@Date: 2021-07-04
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-04 
@Title : Program Aim to concatenate dictionaries to create a new dictionary
'''

from loggers import logger

def concatenate():
    '''
    Description: 
        This function concatenates dictionaries to 
        create a new one
    '''

    try:

        dict1 = {
            0: 10,
            1: 20,
        }

        dict2 = {
            2: 30,
            3: 40
        }

        dict3 = {
            4: 50,
            5: 60
        }

        dict4 = {}

        for d in (dict1, dict2, dict3):
            dict4.update(d)

        logger.info(dict4)
    
    except Exception:
        logger.error("Invalid Input")

if __name__ == "__main__":
    concatenate()