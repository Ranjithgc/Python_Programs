'''
/**********************************************************************************
@Author: Ranjith G C
@Date: 2021-06-26
@Last Modified by: Ranjith G C
@Last Modified time: 2021-06-26
@Title : To check if year is leap year or not
/**********************************************************************************
'''
year = int(input("Enter a year: "))  
if (year % 4) == 0:  
   if (year % 100) == 0:  
       if (year % 400) == 0:  
           print("{0} is a leap year".format(year))  
       else:  
           print("{0} is not a leap year".format(year))  
   else:  
       print("{0} is a leap year".format(year))  
else:  
   print("{0} is not a leap year".format(year))  