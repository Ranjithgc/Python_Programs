from LogHandler import logger
import re
import json

class Validation:

    def validate_name():
        '''
        Description:
            This function implemented for validating name using regex.
        Return:
            this function returns a valid name
        '''

        try:
            name = input("Enter your Name")
            if re.match("^[A-Z]{1}[a-z]*$", name):
                return name
            else:
                logger.error("name should be alphabets")

        except ValueError:
            logger.error("Invalid input")

    def validate_mobile():
        '''
        Description:
            This function implemented for validating mobile number using regex.
        Return:
            this function returns a valid mobile number
        ''' 
        try:
            mobile = input("Enter your Mobile Number")
            if re.match("^[7-9]{1}[0-9]*$", mobile):
                return mobile
            else:
                logger.error("mobile number shpuld be numeric")

        except ValueError:
            logger.error("Invalid input")


    def validate_address():
        '''
        Description:
            This function implemented for validating address using regex.
        Return:
            this function returns a valid address
        '''
        try:
            address = input("Enter your Address")
            if re.match("^[A-Z]{1}[a-z]*$", address):
                return address
            else:
                logger.error("address shpuld be alphabets")

        except ValueError:
            logger.error("Invalid input")

    def validate_zip():
        '''
        Description:
            This function implemented for validating zipcode using regex.
        Return:
            this function returns a valid zipcode
        '''
        try:
            zip = input("Enter your zip")
            if re.match("^[1-9]{1}[0-9]{5}$", zip):
                return zip
            else:
                logger.error("zip shpuld be numeric")

        except ValueError:
            logger.error("Invalid input")

    def validate_city():
        '''
        Description:
            This function implemented for validating city using regex.
        Return:
            this function returns a valid city
        '''
        try:
            city = input("Enter your city")
            if re.match("^[A-Za-z]*$", city):
                return city
            else:
                logger.error("City shpuld be alphabets")

        except ValueError:
            logger.error("Invalid input")

    def validate_state():
        '''
        Description:
            This function implemented for validating state using regex.
        Return:
            this function returns a valid state
        '''
        try:
            state = input("Enter your state")
            if re.match("^[A-Za-z]*$", state):
                return state
            else:
                logger.error("state shpuld be alphabets")

        except ValueError:
            logger.error("Invalid input")
    
    def get_id():
        try:
            while True:
                    id = input(" Enter unique id : ")
                    if re.match("^[0-9]{2,3}$", id):
                        return id
                    else:
                        logger.error("Enter valid id ")
                        
        except ValueError:
            logger.error("Invalid input")

