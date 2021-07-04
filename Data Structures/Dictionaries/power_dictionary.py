'''
@Author: Ranjith G C
@Date: 2021-07-04
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-04 
@Title : Program Aim to to generate and print a dictionary that 
         contains a number (between 1 and n) in the form (x, x*x).
'''

from loggers import logger

def power():
    '''
    Description:
        This function to generate and print a dictionary that 
        contains a number (between 1 and n) in the form (x, x*x).
    '''
    
    try:
        n=int(input("Input a number ")) 
        d = dict()

        for x in range(1,n+1):
            d[x]=x*x

        logger.info(d)

    except ValueError:
        logger.error("Invalid input")

if __name__ == "__main__":
    power()