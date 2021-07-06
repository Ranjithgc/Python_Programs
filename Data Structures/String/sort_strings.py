'''
@Author: Ranjith G C
@Date: 2021-07-06
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-06 
@Title : Program Aim to prints the unique words in sorted form from a comma separated sequence of words
'''
from loggers import logger

try:

    items = input("Input comma separated sequence of words")
    words = [word for word in items.split(",")]
    logger.info(",".join(sorted(list(set(words)))))

except Exception:
    logger.error("Invalid input")