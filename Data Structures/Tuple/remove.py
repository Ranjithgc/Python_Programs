'''
@Author: Ranjith G C
@Date: 2021-07-05
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-05 
@Title : Program Aim to remove element from tuple
'''
from loggers import logger

try:

    #create a tuple
    tuple = ({1,2,3,4,5,6,7,8})
    logger.info(tuple)
    
    #tuples are immutable, so you can not remove elements
    #converting the tuple to list
    list = list(tuple) 
    #use different ways to remove an item of the list
    list.remove(7) 
    #converting the tuple to list
    tuple = tuple(list)
    logger.info(tuple)

except Exception:
    logger.error("Invalid")