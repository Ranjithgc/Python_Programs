"""
@Author: Ranjith G C
@Date: 2021-06-29
@Last Modified By: Ranjith G C
@Last modified Time: 6:30 PM
@Title: simulates Gamblers program
"""
import random

def gambler():
    """
    Description:
        This function Simulates a gambler who start with $stake and place fair $1 bets until
        he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
        times he/she wins and the number of bets he/she makes. Run the experiment N
        times, averages the results, print the results.
    """
    try:
        stake = int(input("Enter gambler`s starting bankroll"))
        goal = int(input("Enter gambler`s desired bankroll"))
        trials = int(input("Enter number of trials to perform"))

        # total number of bets made
        bets = 0
        # total number of games won
        wins = 0

        # repeat trial times
        for t in range(0, trials):
            # do one gmabler`s ruin simulation
            cash = stake
            while cash > 0 and cash < goal:
                bets += 1
                randomnum = random.randint(0,9)
                if( randomnum < 5):
                    # win $1
                    cash += 1
                else:
                    # lose $1
                    cash -= 1
            if(cash == goal):
                wins += 1
    
        print(wins ,"wins of", trials)
        print("Percent of games won = ", 100.0 * wins / trials)
        print("Avg # bets = ", 1.0 * bets / trials)
    except ValueError:
        print()    

gambler()    