from click import edit
import numpy as np
from torch import rand
import shutil

def main():
    NUM_SQUARES = 9
    MAX_SUM = 13
    board = np.zeros(NUM_SQUARES)
    shutil.copy('blankboard.txt', 'gameboard.txt')
    print("Current Board: ")
    with open('gameboard.txt', 'r') as f:
        print(f.read())
    while (board.sum() < MAX_SUM):
        try:
            player = int(input("Enter where to put x from 1 to 9: "))
        except:
            print("Not a valid number. Game Over :((")
            return
        player -= 1
        while ((player < 0) or (player > 8) or (board[player] != 0)):
            player = int(input("Try Again: "))
        board[player] = 1
        editGraphics(board, player)
        with open('gameboard.txt', 'r') as f:
            print(f.read())
        if (checkWinner(board) == 1 or board.sum() == 13):
            print ("You won!")
            return
        input("Press Enter to continue: ")
        print ("Comp's turn")
        comp = np.random.randint(0,9)
        while (board[comp] != 0):
            comp = np.random.randint(0,9)
        board[comp] = 2
        editGraphics(board, comp)
        with open('gameboard.txt', 'r') as f:
            print(f.read())
        if checkWinner(board) == 1:
            print("You lost :(")
            return
    print ("Draw")

def checkWinner(board):
    if board[0] == board[1] == board[2] != 0:
        return 1
    if board[3] == board[4] == board[5] != 0:
        return 1
    if board[6] == board[7] == board[8] != 0:
        return 1
    if board[0] == board[3] == board[6] != 0:
        return 1
    if board[1] == board[4] == board[7] != 0:
        return 1
    if board[2] == board[5] == board[8] != 0:
        return 1
    if board[0] == board[4] == board[8] != 0:
        return 1
    if board[2] == board[4] == board[6] != 0:
        return 1
    return 0

def editGraphics(board, index):
    if board[index] == 1:
        c = 'X'
    else:
        c = 'O'
    file = open('gameboard.txt', 'r')
    full = file.readlines()
    file.close()
    row = 2*(index // 3)
    col = 4*(index % 3) + 2
    curr = full[row]
    full[row] = curr[:col-1] + c + curr[col:]
    file = open('gameboard.txt', 'w')
    file.writelines(full)
    file.close()
    return full
    

main()