'''
@Author: Ranjith G C
@Date: 2021-07-04
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-04 
@Title : Program Aim to implement frozen set 
'''

from loggers import logger

def frozen_set():
    '''
    Description:
        This function clears a set
    '''
    
    # Frozensets
    # initialize A, B and C
    A = frozenset([1, 2, 3, 4])
    B = frozenset([3, 4, 5, 6])
    C = frozenset([5, 6])

    # isdisjoint() method
    logger.info(A.isdisjoint(C))  # Output: True

    # issubset() method
    logger.info(C.issubset(B))  # Output: True

    # issuperset() method
    logger.info(B.issuperset(C))  # Output: True

if __name__ == "__main__":
    frozen_set()        
