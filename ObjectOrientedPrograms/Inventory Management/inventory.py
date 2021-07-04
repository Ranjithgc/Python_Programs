'''
@Author: Ranjith G C
@D Date: 2021-07-03
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-03
@Title : Clinique Management
'''
import json 
import logging

from loggers import logger

class Inventory:

    def __init__(self):
        pass

    def open(self):
        '''
        Description:
            This function opens the json file
        '''
        try:
            with open('inventory.json', 'r+') as file:
                f1 = file.read()
                json_f = json.loads(f1)
                file.close()
            return json_f
        except FileNotFoundError:
            logger.warning("File Not Found")

    def add_inventory(self):
        '''
        Description:
            This function adds the inventory details to json file
        '''
        try:
            dict = {}
            inv_id = input("Enter the Inventory Id")
            name = input("Enter the inventory Name")
            price = input("Enter the Inventory Price")
            weight = input("Enter the Inventory weight")
            with open('inventory.json', 'r') as file:
                f1 = file.read()
                json_f = json.loads(f1)
            dict = {"id": inv_id, "name": name, "price": price, "weight": weight}
            with open('inventory.json', 'w') as file:
                json_f['inventory'].append(dict)
                file.write(json.dumps(json_f, indent=2))
                logger.info("Record Inserted Successfully")
                file.close()
        except ValueError:
            logger.warning("Invalid Input")

    def display_inventory(self, dict):
        '''
        Description: 
            This function displays the inventory details
        '''
        count = 0
        print("Inventory Details \n inventory id \n name \n price \n \n weight")
        for i in range(len(dict['inventory'])):
            inv_id = dict['inventory'][i]['id']
            name = dict['inventory'][i]['name']
            price = dict['inventory'][i]['price']
            weight = dict['inventory'][i]['weight']
            count += 1
            print(' ', count, '\t\t', inv_id, '\t\t', name, '\t\t', price, '\t\t', weight)

    def remove(self, dict):
        '''
        Description:
            This function removes the inventory details from json file
        '''
        try:
            if len(dict['inventory']) >= 1:
                id = int(input("Enter the unique Id"))
                for i in range(len(dict)):
                    if((dict['inventory'][i]['id']) == id):
                        logger.info("Data Removed Successfully")
                        del dict['inventory'][i]
                        with open('inventory.json', 'r') as file:
                            f1 = file.read()
                            json_f = json.loads(f1)
                        with open('inventory.json', 'w') as file:
                            json_f['inventory'].append(dict)
                            file.write(json.dumps(json_f, indent=2))
                        logger.info("Record Deleted Successfully")
                        file.close()
                        return 
        except Exception as e:
            logger.error(e)

if __name__ == "__main__":
    try:
        data = Inventory()
        dict = data.open()
        while True:
            choice = int(input("1.Add Inventory \n 2. Display Inventory \n 3. Remove Inventory \n 4. Exit \n "))
            if(choice == 1):
                data.add_inventory()
            if(choice == 2):
                data.display_inventory(dict)
            if(choice == 3):
                data.remove(dict)
            if(choice == 4):
                exit()
    except ValueError:
        logger.warning("Invalid Input")
    except TypeError:
        logger.warning("Invalid")