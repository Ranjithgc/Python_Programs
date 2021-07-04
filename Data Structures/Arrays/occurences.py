'''
@Author: Ranjith G C
@Date: 2021-07-04
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-04 
@Title : Program Aim to find the occurences of specified number in an array
'''
from loggers import logger

def occurences(myArray, key):
    '''
    Description:
        This function implemented to find the number of 
        occurence of an given number.
    Parameter:
        myArray and key takes to find the occurences. 
    '''
    
    try:
        count = 0
        
        for i in range(len(myArray)):
            if myArray[i] == key :
                count += 1 
        
        print('The Number of Occurences of', key ,'is: ' ,count,'times')

    
    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    
    try:
        arr = [1,2,3,4,5,3,7,3,8,3]
        number = 3
        occurences(arr, number)
    
    except Exception:
        logger.error("Invalid input")
