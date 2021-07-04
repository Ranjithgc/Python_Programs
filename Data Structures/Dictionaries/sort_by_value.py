'''
@Author: Ranjith G C
@Date: 2021-07-04
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-04 
@Title : Program Aim to sort by value in dictionary 
         by ascending and descending order.
'''
from loggers import logger

def sort_by_value():
    '''
    Description:
        This function used to sort the values in dictionary
        by ascending and descending order. 
    '''
    
    try:
        
        a = {'a': 2,
             'b': 1,
            'c': 3,
            'd': 5,
            'e': 4
            }

        logger.info("Sort by Ascending Order")
        logger.info(sorted(a.values()))

        logger.info("Sort by Descending Order")
        logger.info(sorted(a.values(), reverse= True))
    
    except Exception:
        logger.error("Invalid Input")

if __name__ == "__main__":
    sort_by_value()