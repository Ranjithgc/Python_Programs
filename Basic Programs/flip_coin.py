'''
/**********************************************************************************
@Author: Ranjith G C
@Date: 2021-06-26
@Last Modified by: Ranjith G C
@Last Modified time: 2021-06-26
@Title : Flip coin and print percentage of heads and tails
/**********************************************************************************
'''
import random

flip_number = int(input("Enter count of flip coin - "))
heads_count = 0
tails_count = 0

for count in range(0,flip_number):
    flip_coin_result = random.randint(0,1)

if flip_coin_result < 0.5:
    tails_count += 1
else:
    heads_count += 1

tails_percent = (tails_count/flip_number) * 100
heads_percent = (heads_count/flip_number) * 100

print("Tails percentage - ", tails_percent)
print("Heads percentage - ", heads_percent)
