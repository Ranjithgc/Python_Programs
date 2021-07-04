'''
@Author: Ranjith G C
@Date: 2021-07-04
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-04 
@Title : Accessing the Array and Display the Array
'''
import array
import logging
from loggers import logger

def display(myArray):
    '''
    Description:
        This function is implemented to display the array
    Parameter:
        myArray to iterate the elements and to access the Array elements 
    '''
    try:
        for i in range(len(myArray)):
            logger.info(myArray[i])
    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    try:
        myArray = array.array("i",[10,12,15,17,21])
        display(myArray)
    except Exception:
        logger.error("Invalid")