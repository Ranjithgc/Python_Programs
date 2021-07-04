'''
@Author: Ranjith G C
@Date: 2021-07-04
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-04 
@Title : Program Aim to check multiple keys exists in a dictionary
'''

from loggers import logger

def multiple_keys():
    '''
    Description:
        This function to check multiple keys exists in a dictionary
    '''

    student = {
    'name': 'Ranjith',
    'class': 'V',
    'roll_id': '2'
    }
    
    logger.info(student.keys() >= {'class', 'name'})
    logger.info(student.keys() >= {'name', 'Ranjith'})
    logger.info(student.keys() >= {'roll_id', 'name'})

if __name__ == "__main__":
    multiple_keys()
