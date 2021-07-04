'''
@Author: Ranjith G C
@Date: 2021-07-04
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-04 
@Title : Program Aim to print a dictionary in table format
'''

from loggers import logger

def table_format():
    '''
    Description:
        This function to print a dictionary in table format
    '''
    
    try:
    
        dict ={}

        # Insert data into dicitonary
        dict1 = {1: ["Samuel", 21, 'Data Structures'],
	        2: ["Richie", 20, 'Machine Learning'],
	        3: ["Lauren", 21, 'OOPS with java'],
	    }

        logger.info("{:<10} {:<10} {:<10}".format('NAME', 'AGE', 'COURSE'))

        # print each data item.
        for key, value in dict1.items():
	        name, age, course = value
	        logger.info("{:<10} {:<10} {:<10}".format(name, age, course))
    
    except Exception:
        logger.error("Invalid Input")

if __name__ == "__main__":
    table_format()