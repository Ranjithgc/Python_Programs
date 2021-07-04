'''
@Author: Ranjith G C
@Date: 2021-07-04
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-04 
@Title : Program Aim to remove a key from a dictionary
'''

from loggers import logger

def remove_key():
    '''
    Description:
        This function removes a key from a dictionary
    '''
    try:
    
        myDict = {'a':1,
        'b':2,
        'c':3,
        'd':4
        }
    
        print(myDict)
        if 'a' in myDict: 
            del myDict['a']
        logger.info(myDict)

    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    remove_key()