'''
@Author: Ranjith G C
@Date: 2021-07-06
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-06 
@Title : Program Aim to Display Formatted Text
'''
from loggers import logger

try:
    str1 = 'The quick brown fox jumps over the lazy dog.'
    logger.info(str1.count("fox"))
    
except Exception:
    logger.error()