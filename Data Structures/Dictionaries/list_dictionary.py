
'''
@Author: Ranjith G C
@Date: 2021-07-04
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-04 
@Title : Program Aim to convert list into nested dictionary of keys
'''

from loggers import logger

def convert_to_dictionary():
    '''
    Description:
        This function converts list into nested
        dictionary of keys
    '''
    num_list = [1, 2, 3, 4]
    new_dict = current = {}
    
    for name in num_list:
        current[name] = {}
        current = current[name]
    
    logger.info(new_dict)

if __name__ == "__main__":
    convert_to_dictionary()