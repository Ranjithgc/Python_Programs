"""
@Author: Ranjith G C
@Date: 2021-06-29
@Last Modified By: Ranjith G C
@Last modified Time: 2:00 PM
@Title: Generating Coupon Numbers
"""

import random
import math

def checkValue(randomNum, couponNumber):
    """
    Description:
        This function Checks how many random Number needs to generate distinct
        coupon number
    Parameter:
        this function takes randomNum, couponNumber as arguments
    Return:
        This function returns the boolean value
    """
    for i in range(0, len(couponNumber)):
        if(couponNumber[i] == randomNum):
            return True
    return False

def coupon():
    """
    Description:
        This function gives how many random number needs to generate 
        coupon number
    """
    couponNumber = [2, 4, 6, 8]
    randomList = len(couponNumber)
    totalRandoms = 0
    checkCount = 0
    while checkCount < len(couponNumber):
        print(checkCount)
        totalRandoms += 1
        randomNum = random.randint(0,9)
        print("Random Value :", randomNum)
        if(checkValue(randomNum, couponNumber) and not(checkValue(randomNum, couponNumber))):
            randomList[checkCount] = randomNum
            checkCount += 1
    print("Total Randoms ", totalRandoms)

coupon()
    