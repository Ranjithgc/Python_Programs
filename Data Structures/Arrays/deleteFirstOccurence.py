'''
@Author: Ranjith G C
@Date: 2021-07-04
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-04 
@Title : Program Aim to delete the first occurences of specified number in an array
'''

from loggers import logger

def delete_occurence(myArray, key):
    '''
    Description:
        This function removes the first occurence element 
        in an array.
    Parameter:
        It takes myArray and key to remove first occurence
    '''
    try:
        for i in range(len(myArray)):
            if myArray[i] == key:
                myArray.remove(key)
                break
        print("Array after removing", key, ' is', myArray)

    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    try:
        arr = [1,2,3,4,5,3,7,3,8,3]
        number = 3
        delete_occurence(arr, number)
    
    except Exception as e:
        logger.error(e)
            
