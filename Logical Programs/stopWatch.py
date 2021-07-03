"""
@Author: Ranjith G C
@Date: 2021-06-29
@Last Modified By: Ranjith G C
@Last modified Time: 3:00 PM
@Title: simulates stopwatch problem
"""
import datetime

def stopWatch():
    """
    Description:
        This function measuring the time that elapses between 
        start and end clicks
    """
    input("Press Enter to start")
    start_time = datetime.datetime.now()

    input("Press Enter to stop")
    end_time = datetime.datetime.now()

    time_lapsed = end_time - start_time
    print(time_lapsed)

stopWatch()