'''
@Author: Ranjith G C
@D Date: 2021-07-01
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-01
@Title : Clinique Management
'''
import json 
import logging

from loggers import logger
from Validation import Validation

class CliniqueManagement:
    def _init__(self):
        pass

    def doctor_info(self):
        '''
        Description:
            This function implemented for opening the doctor json file.
        Return:
            it returns json file
        '''
        try:
            with open('doctors.json', 'r+') as file:
                file1 = file.read()
                jsonf1 = json.loads(file1)
                file.close()
            return jsonf1
        except FileNotFoundError:
            logger.error("File Not Found")

    def patient_info(self):
        '''
        Description:
            This function implemented for opening the patients json file.
        Return:
            it returns json file
        '''
        try:
            with open('patients.json', 'r+') as file:
                file1 = file.read()
                jsonf1 = json.loads(file1)
                file.close()
            return jsonf1
        except FileNotFoundError:
            logger.error("File Not Found")

    def search_doctor(self, doctor_info):
        """
        Description:
            This function gives the information about the doctors based on input provided by user as
            name, specialization, availability.
        Parameters:
            It takes doctor_data as parameter where we have loaded json file
        Return:
            It returns list of attributes of doctor
        """
        doct = input("Enter details to search doctor by name, specialization, qualification: ")
        list = []
        for doctor in doctor_info['doctor']:
            if doct in doctor.values():
                name = doctor['name']
                id = doctor['Id']
                specialization = doctor['specialization']
                availability = doctor['availability']
                doctor_detail = {
                    "name": name,
                    "Id": id,
                    "availability": availability,
                    "specialization": specialization
                }
                print(f"Id: {id} \nName: {name} \nSpecialization: {specialization} \nAvailability: {availability}")
                logger.info(f"Name: {name} \nSpecialization: {specialization} \nAvailability: {availability}")
                list.append(doctor_detail)
        return list

    def appointment(self,doctor_info, patient_info):
        """
        Description:
            This function is to book appointment with doctor by serching doctor by its attributes.
        Parameters:
            It takes doctor_data, patient_data as parameter where we have loaded json file
        """
        # check for attribute is present or not
        doctor_list = self.search_doctor(doctor_info)
        if not doctor_list:
            print("No doctor present")
            self.appointment(doctor_info, patient_info)
        
        # Patient Detail            
        name = Validation.validateName()
        number = Validation.validateNumber()
        id = 0
        for data in patient_info['patient']:
            id = data['Id']
        patient_detail = {
            "Id": id+1,
            "Name": name,
            "mobile_number": number
        }
        
        # appending the patient data
        patient_info['patient'].append(patient_detail)
        # adding patient details to doctors patient list
        for doctor in doctor_info['doctor']:
            if id == doctor['Id']:
                doctor['total_patients'] += 1
                doctor['patients'].append(patient_detail)
        # writing to json file
        patient_detail = self.patient_info()
        
        #writing to json file
        doctor_list = self.doctor_info()
        
        logger.info("Appointment booked successfully!!")
        logger.info(f"Appointment booked for {patient_detail}")
        return
    
    def search_patient(self, patient_info):
        """
        Description:
            This function gives the information about the patient based on input provided by user as
            name, number, id.
        Parameters:
            It takes patient_data as parameter where we have loaded json file
        """
        pat = input("Enter the Patient name")
        list = []
        for patient in patient_info['patient']:
            if pat in patient.values():
                name = patient['Name']
                id = patient['Id']
                age = patient['Age']
                number = patient['mobile_number']
                patient_detail = {
                    "Name": name,
                    "Id": id,
                    "Age": age,
                    "mobile_number": number
                }
                print(f"Name: {name} \nNumber: {number} \nAge: {age} \nMobile: {number} ")
                logger.info(f"Name: {name} \nNumber: {number} \nAge: {age} \nMobile: {number} ")
                list.append(patient_detail)
                return list

    def main(self):
        """
        Description:
            This is main function it will call other methods to execute.
            It will ask user to make choice and accordingly call methods
        """
        print("Select Operation 1.Search Doctor 2.Search Patient 3.Book Appointment: ")
        choice = int(input())
        doctor = self.doctor_info()
        patient = self.patient_info()
        if choice == 1:
            self.search_doctor(doctor)
        if choice == 2:
            self.search_patient(patient)
        if choice == 3:
            self.appointment(doctor, patient)

        print("Do you want to try again? 1.Yes  2.No")
        choice = int(input())
        if choice == 1:
            self.main()
        else:
            return

if __name__ == '__main__':
    clinic = CliniqueManagement()
    clinic.main()