'''
@Author: Ranjith G C
@Date: 2021-07-04
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-04 
@Title : Program Aim to count the values associated with key
'''

from loggers import logger

def count_values():
    '''
    Description: 
        This function counts the values associated with key
    '''
    try:

        student = [{'id': 1, 'success': True, 'name': 'Lary'},
        {'id': 2, 'success': False, 'name': 'Rabi'},
        {'id': 3, 'success': True, 'name': 'Alex'}]
    
        logger.info(sum(d['id'] for d in student))
    
        logger.info(sum(d['success'] for d in student))
    
    except Exception:
        logger.error("Invalid")

if __name__ == "__main__":
    count_values()