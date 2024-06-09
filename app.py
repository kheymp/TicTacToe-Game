import sys
import random
import time

originalBoard = ["-", "-", "-",
                "-", "-", "-",
                "-", "-", "-"]

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentPlayer = "X"
winner = None
gameRunning = True
playWithComputer = True
def printBoard(board):
    for index, array in enumerate(board):
        print(array, end="")
        if not(index + 1) % 3 == 0:
            print(" | ", end="")
        if (index + 1) % 3 == 0:
            print()
            if index + 1 < len(board):
                print("----------")

def playerInput(board):
    try:
        inp = int(input("Enter a number (1-9): "))

        if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
            board[inp - 1] = currentPlayer
        elif not (inp >= 1 and inp <= 9):
            print("Invalid range selected.")
            playerInput(board)
        elif not (board[inp - 1] == "-"):
            print("Spot already selected.")
            playerInput(board)
        else:
            print("Unknown error occured.")
            sys.exit()
    except ValueError as e:
        print("Invalid value entered.")
        playerInput(board)

def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[6] == board[4] == board[2] and board[6] != "-":
        winner = board[6]
        return True

def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It's a tie")
        gameRunning = False
        playAgain()

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

def checkWin():
    if checkHorizontal(board) or checkDiagonal(board) or checkVertical(board) == True:
        printBoard(board)
        print(f"The winner is {winner}")
        playAgain()

def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()

def playAgain():
    global gameRunning
    global board
    global winner
    global currentPlayer

    try:
        play = input("Play again? (Y/N): ")
        if play.lower() == "y":
            gameRunning = True
            board = originalBoard
            winner = None
            currentPlayer = "X"
            startGame()
        elif play.lower() == "n":
            gameRunning = False
            sys.exit()
        else:
            print("Invalid input")
            playAgain()
    except ValueError as e:
        playAgain()

def startGame():
    global playWithComputer


    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()

    if playWithComputer:
        computer(board)

    checkWin()
    checkTie(board)

try:
    inp = input("Play with computer? (Y/N): ")
    if inp.lower() == "y":
        playWithComputer = True
    elif inp.lower() == "n":
        playWithComputer = False
    else:
        print("Invalid value.")
        startGame()
except KeyboardInterrupt as e:
    print("Exiting gracefully.")
    sys.exit(0)
except ValueError as e:
        print("Invalid value.")
        startGame()


while gameRunning:
    try:
        startGame()
    except KeyboardInterrupt:
        print("Exiting gracefully.")
        sys.exit(0)








# printing the game board

# take player input

# check for win or tie

# switch the player

# check for win or tie again