'''
@Author: Ranjith G C
@Date: 2021-07-05
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-05 
@Title : Program Aim to Print a list after removing specified elements
'''
from loggers import logger
import itertools

try:
    
    list1 = [1, 2, 3]
    permutation = itertools.permutations(list1)
    list2 = list(permutation)
    logger.info(list2)

except Exception as e:
    logger.error(e)