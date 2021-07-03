'''
/**********************************************************************************
@Author: Ranjith GC
@Date: 2021-06-26
@Last Modified by: Ranjith GC
@Last Modified time: 2021-06-26
@Title : To replace given string
/**********************************************************************************
'''
username = input("enter Username - ")
# check if username have minimum 3 characters
if len(username) > 3:
    string_template = f"Hello {username}, How are you?" #string formating
else:
    print("Username should be of 3 characters")

print(string_template)