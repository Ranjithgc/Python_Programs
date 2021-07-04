'''
@Author: Ranjith G C
@Date: 2021-07-04
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-04 
@Title : Program Aim to print unique values in a dictionary
'''

from loggers import logger

def unique_values():
    '''
    Description:
        This function prints unique values in a dictionary
    '''

    try:
       
        test_list = [{'gfg' : 1, 'is' : 2}, {'best' : 1, 'for' : 3}, {'CS' : 2}]
        print("The original list : " +  str(test_list))

        # Using set() + values() + dictionary comprehension
        # Get Unique values from list of dictionary
        res = list(set(val for dic in test_list for val in dic.values()))

        logger.info("The unique values in list are : " + str(res))

    except Exception:
        logger.error("Invalid Input")

if __name__ == "__main__":
    unique_values()