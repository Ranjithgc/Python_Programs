'''
/**********************************************************************************
@Author: Ranjith G C
@Date: 2021-06-26
@Last Modified by: Ranjith G C
@Last Modified time: 2021-06-26
@Title : To print the table of power of two with given input
/**********************************************************************************
'''
end_power_value = int(input("Enter end value of power - "))
    
#check if input is in range of 0 to 31
if (0 <= end_power_value < 31):
    for power_value in range(0, end_power_value+1):
        generate_number = 2**power_value
        print("2^" + str(power_value) + " = " + str(generate_number))
        
else:
    print("Please enter number less than 31 and greater than or equal to 0 ")