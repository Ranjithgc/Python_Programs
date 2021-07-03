"""
@Author: Ranjith G C
@Date: 2021-06-28
@Last Modified by: Ranjith G C
@Last Modified time: 2021-06-28
@Title : program WindChill.java that takes two double command-line arguments t
and v and prints the wind chill. Use Math.pow(a, b) to compute ab. Given the
temperature t (in Fahrenheit) and the wind speed v (in miles per hour), the
National Weather Service defines the effective temperature (the wind chill) to be:
"""
import math

def calculate_wind_chill():
    """
    Description:
        This function is used for calculating wind chill. 
        It takes a user input of temperature and wind speed for calculating wind chill.   
    """

    try:
        temperature = float(input("Enter the Temperature from '0' to '50': "))
        wind_Speed = float(input("Enter the Wind Speed between '3' to '120' : "))
        print(temperature)

        if ((temperature) > 40 or wind_Speed > 100 or wind_Speed < 3):
            print("Please give the Valid input as Shown in the Statement above!!")
            calculate_wind_chill()
        else:
            windChill = 35.74 + 0.62158 * temperature + (0.4275 * temperature - 35.75) * math.pow(wind_Speed, 0.16)
            print("The National Weather Service defines the effective temperature (the wind chill) to be: ", windChill)

    except ValueError:
        print("Enter a valid Integer values")

calculate_wind_chill()