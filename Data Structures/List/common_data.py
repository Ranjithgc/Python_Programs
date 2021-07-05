'''
@Author: Ranjith G C
@Date: 2021-07-05
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-05 
@Title : Program Aim to Takes two lists and returns True
         if they have at least one common member
'''

from loggers import logger

def common_data(list1, list2):
    '''
    Description:
        This function Takes two lists and returns True 
        if they have at least one common member 
    Parameter:
        it takes list1,list2 2 parameters. 
    Return:
        it returns true. 
    '''
    try:

        result = False
        for x in list1:
            for y in list2:
                if x == y:
                    result = True
                    return result
    
    except Exception:
        logger.error("Invalid Input")

list1 = [1,2,3,4,5,6]
list2 = [1,2,7,8,9]
list3 = [7,8,9]
logger.info(common_data(list1, list2))
logger.info(common_data(list1, list3))