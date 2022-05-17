# -*- coding: utf-8 -*-
"""
Created on Sun May 15 08:54:01 2022

@author: lizzomatic
"""

ALL_SPACES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
X, O, BLANK = 'X', 'O', ' '

def main():
    print("Let\'s Play TIC-TAC-TOE:")
    gameBoard = getBlankBoard()
    currentPlayer, nextPlayer = X, O
    
    while True:   #main game loop
        print(getBoardStr(gameBoard))   #Display the board
        move = None
        print('It\'s {}\'s turn:'.format(currentPlayer))
        #print available moves
        print("available moves: ")
        print(*availableMoves(gameBoard), sep = ", ")
        #
        if winMove(gameBoard, currentPlayer):
            print("play here to win: ") 
            print(*winMove(gameBoard, currentPlayer), sep = ', ')
        
        if winMove(gameBoard, nextPlayer):
            print("play here to not lose: ")
            print(*winMove(gameBoard, nextPlayer), sep = ', ')
        while not isValidSpace(gameBoard, move):
            print('{}, make your move: (1-9)'.format(currentPlayer))
            move = input('> ')
        updateBoard(gameBoard, move, currentPlayer)   #make move
        
        #check if there's a winner:
        if isWinner(gameBoard, currentPlayer):   #check for a winner
            print(getBoardStr(gameBoard))
            print(currentPlayer + ' has won the game!')
            break
        elif isBoardFull(gameBoard):   #Check for a tie
            print(getBoardStr(gameBoard))
            print('The game is a tie!')
            break

        #Switch players
        currentPlayer, nextPlayer = nextPlayer, currentPlayer
    print('Thanks for playing!')
    
def getBlankBoard():
    #
    board = {}
    for space in ALL_SPACES:
        board[space] = BLANK
    return board

def getBoardStr(board):
    return '''
        {}|{}|{}   1 2 3
        -+-+-
        {}|{}|{}   4 5 6
        -+-+-
        {}|{}|{}   7 8 9'''.format(board['1'], board['2'], board['3'],
                                 board['4'], board['5'], board['6'],
                                 board['7'], board['8'], board['9'])

#returns True if the space is valid space number and blank
def isValidSpace(board, space):
    return space in ALL_SPACES and board[space] == BLANK

#returns True if the player is a winner
def isWinner(board, player):
    b, p = board, player
    # check for 3-in-a row, colum, diagonal
    return((b['1'] == b['2'] == b['3'] == p) or #top row
           (b['4'] == b['5'] == b['6'] == p) or #midde row
           (b['7'] == b['8'] == b['9'] == p) or #bottom row
           (b['1'] == b['4'] == b['7'] == p) or #left column
           (b['2'] == b['5'] == b['8'] == p) or #middle column
           (b['3'] == b['6'] == b['9'] == p) or #right column
           (b['3'] == b['5'] == b['7'] == p) or #diagonal
           (b['1'] == b['5'] == b['9'] == p))   #diagonal


#returns a list of potential win moves for a specific player
def winMove(board, player):
    b, p = board, player
    winMoves = [] #initialize an empty list of win moves
    #list potential win rows - list of lists of dictionary keys
    wR = [[b['1'], b['2'], b['3']], #top row
           [b['4'], b['5'], b['6']], #midde row
           [b['7'], b['8'], b['9']], #bottom row
           [b['1'], b['4'], b['7']], #left column
           [b['2'], b['5'], b['8']], #middle column
           [b['3'], b['6'], b['9']], #right column
           [b['3'], b['5'], b['7']], #diagonal
           [b['1'], b['5'], b['9']]] #diagonal
    #same list of potential win rows as a list of lists of numbers
    wRL = [[1, 2, 3], #top row
           [4, 5, 6], #midde row
           [7, 8, 9], #bottom row
           [1, 4, 7], #left column
           [2, 5, 8], #middle column
           [3, 6, 9], #right column
           [3, 5, 7], #diagonal
           [1, 5, 9]] #diagonal                  
    #loop through potential winRows to check for potential win
    for x in range(0, len(wR)):
        if wR[x][0] == wR[x][1] == p and wR[x][2] == BLANK:
            winMoves.append(wRL[x][wR[x].index(BLANK)])
        elif wR[x][0] == wR[x][2] == p and wR[x][1] == BLANK:
            winMoves.append(wRL[x][wR[x].index(BLANK)])
        elif wR[x][1] == wR[x][2] == p and wR[x][0] == BLANK:
            winMoves.append(wRL[x][wR[x].index(BLANK)]) 
    return winMoves
    
#returns True if the board is full
def isBoardFull(board):
    for space in ALL_SPACES:
        if board[space] == BLANK:
            return False   #returns False if any space is blank
    return True   #returns True if no spaces are blank

#sets a space to a mark    
def updateBoard(board, space, player):
    board[space] = player
    
def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False

#returns a list of all available moves
def availableMoves(board):
    moves = []
    for x in board:
        if board[x] == BLANK:
            moves.append(x)
    return moves
        
if __name__ == '__main__':
    main()