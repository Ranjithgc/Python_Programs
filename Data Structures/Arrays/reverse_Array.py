'''
@Author: Ranjith G C
@Date: 2021-07-04
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-04 
@Title : Program Aim to Reverse an Array
'''
from loggers import logger

def reverse(arr):
    '''
    Description:
        This function reverse the elements of an array
    Parameter:
        arr to iterate the elements and reverse the elements
    '''

    #Loop through the array in reverse order    
    for i in range(len(arr)-1, -1, -1):     
        logger.info(arr[i])

if __name__ == "__main__":
    try:
        arr = [1, 2, 3, 4, 5];     
        logger.info("Original array: ");    
    
        for i in range(0, len(arr)):    
            logger.info(arr[i]),     
        
        logger.info("Array in reverse order: "); 
        reverse(arr) 

    except Exception:
        logger.error("Invalid input")