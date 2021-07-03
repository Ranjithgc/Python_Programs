'''
@Author: Ranjith G C
@Date: 2021-07-01 18:00:30
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-03 
@Title : Address Book Problem
'''
import json 
import sys
import logging

from LogHandler import logger
from Validation import Validation 

class AddressBook:
   

    def __init__(self):
        self.list = []
                 

    def open(self):
        """
    Description:
        This method is used for opening and loading stored details from a json file.
    Parameter:
        It takes self as a parameter and load all the data from json file to a list.
       
    """

        try:

            with open('addressbook.json', 'r') as file:
                self.list = json.load(file)

        except FileNotFoundError:
            logger.error('Invalid file name')
            

    def add(self):
        """
    Description:
        This method is used for adding a address book details in address book.
        it creates a dictionary and add details into it and then append them to a list.
    Parameter:
        It takes self as a parameter and append details into list.
       
    """
        addNew = {}
        id = Validation.get_id()
        addNew['id'] = id
        name = Validation.validate_name()
        addNew['name'] = name
        mobile = Validation.validate_mobile()
        addNew['mobile'] = mobile
        address = Validation.validate_address()
        addNew['address'] = address
        zip = Validation.validate_zip()
        addNew['zip'] = zip
        city = Validation.validate_city()
        addNew['city'] = city
        state = Validation.validate_state()
        addNew['state'] = state
        self.list['data'].append(addNew)
        self.save()

    def save(self):
        """
    Description:
        This method is writing or storing address book details from list into json file
    Parameter:
        It takes self as a parameter to get addressbook details stored inside list and
        using json dump it writes those details inside json file.
       
    """
        try:
            with open('addressbook.json', 'w+') as file:
                json.dump(self.list, file, indent=2)
                logger.info("file successfully saved...")
        
        except Exception as e:
            logger.error(e)

        finally:
                file.close()
            

    def update(self):
        """
    Description:
        This method is used for update addressbook details from the json file
    Parameter:
        It takes self as a parameter to get addressbook details stored inside list and
        update the details and save them into json file.
       
    """
        try:
            
            flag = updateDetails = False
            if len(self.list['data']) >= 1:
                id = input("Enter Your Unique id : ")
                for i in range(len(self.list['data'])):
                    if (self.list['data'][i]['id'] == id):
                        flag = True
                        if flag:
                            option = int(
                            input(" Select Any One Option to update your Profile\n 1 First Name \n 2 Last Name \n 3 Mobile Number\n 4 Address \n 5 Zipcode \n 6 city \n 7 state \n "))

                            if option == 1:
                                name = Validation.validate_name()
                                self.list['data'][i]['name'] = name
                                self.save()
                                updateDetails = True

                            elif option == 2:
                                mobile = Validation.validate_number()
                                self.list['data'][i]['mobile'] = mobile
                                self.save()
                                updateDetails = True

                            elif option == 4:
                                address = Validation.validate_address()
                                self.list['data'][i]['address'] = address
                                self.save()
                                updateDetails = True

                            elif option == 5:
                                zip = Validation.validate_zip()
                                self.list['data'][i]['zip'] = zip
                                self.save()
                                updateDetails = True

                            elif option == 6:
                                city = Validation.validate_city()
                                self.list['data'][i]['city'] = city
                                self.save()
                                updateDetails = True

                            elif option == 7:
                                state = Validation.validate_state()
                                self.list['data'][i]['state'] = state
                                self.save()
                                updateDetails = True

                            else:
                                print("Invalid Option")
                                updateDetails = False
                                self.update()

        except ValueError:
                        logger.error("Enter a valid option")
                        updateDetails = False
                        self.update()

        except Exception as e:
            logger.error(e)
            self.update()


    def remove(self):
        """
    Description:
        This method is used for deleting address book details from the json file.
    Parameter:
        It takes self as a parameter to get addressbook details stored inside list and
        delete the details and saved the json file.
       
    """ 
        try:
            if len(self.list['data']) >= 1:
                id = input("Enter Your Unique id : ")
                for i in range(len(self.list['data'])):
                    if ((self.list['data'][i]['id']) == id): 
                        logger.info(" Data Removed Successfully ")
                        del self.list['data'][i]
                        self.save()
                        return
                    
        except Exception as e:
            logger.error(e)


    def display(self):
        """
    Description:
        This method is used for displaying addressbook details from a json file
    Parameter:
        It takes self as a parameter to get addressbook details stored inside list and
        display all the stored details.
       
    """
        logger.info(self.list)
        if len(self.list['data']) >= 1:
            logger.info("Data in the file is Given below: \n")
            logger.info('Id \t\t\t\t Name \t\t\t\t  Mobile \t\t\t\t\t Adress \t\t\t\t Zipcode \t\t\t\t\t City \t\t\t\t\t State \n')
            try:
                for i in range(len(self.list['data'])):
                    logging.info(self.list['data'][i]['id'], "\t\t\t\t", self.list['data'][i]['name'],  "\t\t\t\t",
                        self.list['data'][i]['mobile'], "\t\t\t\t", self.list['data'][i]['address'], "\t\t\t\t",
                        self.list['data'][i]['zip'], "\t\t\t\t", self.list['data'][i]['city'], "\t\t\t\t",
                        self.list['data'][i]['state'], "\n")
            except ValueError:
                logging.warning("Invalid Key")

        else:
            logging.warning("No data found")
            ch = input('do you want to Add new record? : Enter = y/n ')
            if ch.upper() == 'y' or ch == 'yes' or ch == 'Yes':
                self.add()
            else:
                sys.exit()
           
if __name__ ==  '__main__':
    try:
        while True:
            address = AddressBook() # Assigning the object to address class
            op = int(input("Press \n 1. To Existing User 2. To New User 3. To Quit \n"))
            if op == 1:
                address.open() # opening the file
                choice = int(input(' Press \n 1. To Add new contact \n 2. To Delete\n 3. To Update address book\n'
                                   ' 4. To Print Book \n' ' 5. To Quit \n '))  # Asks user for input
                if choice == 1:
                    address.add()
                    logger.info(" Data Added Successfully ")  # if user input is 1 the add a data
                elif choice == 2:
                    address.remove()
                    logger.info(" Data Removed Successfully ")  # if user input is 2 then delete a data
                elif choice == 3:
                    address.update()
                    logger.info(" Data Updated Successfully ")  # user input is 3 to update the data
                elif choice == 4:
                    address.display()
                    logger.info(" Data is Currently Displaying ")  # user input is 4 to print the AddressBook
                elif choice == 5:
                    logger.info(" Bye User ")
                    exit()
            elif op == 2:
                address.add()
            elif op == 3:
                exit()
    except KeyboardInterrupt:
        logger.error("\nForce Quit ")
        logger.error(" Bye ")
    except ValueError:
        logger.error("Invalid Option")            
          
