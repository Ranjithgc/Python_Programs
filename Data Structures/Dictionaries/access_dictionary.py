'''
@Author: Ranjith G C
@Date: 2021-07-04
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-04 
@Title : Program Aim to add a key to dictionary
'''
from loggers import logger

def access_dictionary():

    '''
    Description:
        This function implemented types of accessing 
        dictionary.
    '''

    statesAndCapitals = {
                     'Karnataka': 'Banglore',
                     'Maharashtra' : 'Mumbai',
                     'Rajasthan' : 'Jaipur',
                     'Bihar' : 'Patna'
                    }
                      
    print('List Of given states and their capitals:\n')
  
    # Iterating over values
    for state, capital in statesAndCapitals.items():
        logger.info(state, ":", capital)

    dict1 = {
        'a': 'juice',
        'b': 'grill',
        'c': 'corn'
    }

    # Return keys or values explicitly
    for keys in dict1.keys():
        logger.info(keys)

    for values in dict1.values():
        logger.info(values)

if __name__ == "__main__":
    access_dictionary()