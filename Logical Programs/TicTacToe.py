"""
@Author: Ranjith G C
@Date: 2021-06-29
@Last Modified By: Ranjith G C
@Last modified Time: 8:00 PM
@Title: Tic Toc Toe Game
"""
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
player = 1

win = 1
draw = -1
running = 0
stop = 1

game = running
mark = 'X'

def drawBoard():
    """
    Description:
        This Function Draws Game Board
    """
    print(" %c | %c | %c " % (board[1],board[2],board[3]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[4],board[5],board[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[7],board[8],board[9]))    
    print("   |   |   ")

def checkPosition(x):
    """
    Description:
        This Function checks position is empty or not
    """
    if(board[x] == ' '):
        return True
    else:
        return False

def checkWin():
    """
    Description:
        This Function Checks player has won or not
    """
    global game
    # Horizontal Winning condition
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
        game = win
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
        game = win
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
        game = win
    
    # Vertical Winning Condition
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        game = win
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        game = win
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
        game = win

    # Diagonal Winning Condition
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):
        game = win
    elif(board[3] == board[5] and board[5] == board[9] and board[5] != ' '):
        game = win

    # Match Tie or Draw Condition 
    elif(board != ' ' and board[2] != ' ' and board[3] != ' '
        and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' 
        and board[7] != ' ' and board[8] != ' ' and board[9] != ' '):
        game = draw
    else:
        game = running

print("Tic Tac Toe Game.......")
print("Player 1 [X] --- player 2 [O]\n")
while(game == running):
    drawBoard()
    if(player % 2 != 0):
        print("Player 1`s chance")
        mark = 'X'
    else:
        print("Player 2`s chance")
        mark = 'O'
    choice = int(input("Enter the position between [1-9] where you want to mark : "))    
    if(checkPosition(choice)):
        board[choice] = mark
        player += 1
        checkWin()

drawBoard()
if(game == draw):
    print("Game Draw")
elif(game == win):
    player -= 1
    if(player % 2 != 0):
        print("Player 1 Won")
    else:
        print("Player 2 Won")