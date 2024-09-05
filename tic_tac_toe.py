import numpy as np
board = np.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1_symbol = 'X'
p2_symbol = 'O'

def place(symbol):
    print(np.matrix(board)) # it will print the rows in matrix form
    while(1):
        row = int(input("Enter row number-1,2,3:"))
        col = int(input("Enter column number-1,2,3:"))
        if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-':
            break
        else:
            print('Invalid input, Please enter again!')
    board[row-1][col-1]=symbol

def won(symbol):
    return check_rows(symbol) or check_cols(symbol) or check_diagonals(symbol)

def check_rows(symbol):
    for r in range(3):
        count = 0
        for c in range(3):
            if board[r][c] == symbol:
                count += 1
        if count==3:
            print(symbol, 'WON')
            return True
    return False

def check_cols(symbol):
    for c in range(3):
        count = 0
        for r in range(3):
            if board[r][c] == symbol:
                count += 1
        if count==3:
            print(symbol, 'WON')
            return True
    return False

def check_diagonals(symbol):
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==symbol:
        print(symbol,'WON')
        return True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]==symbol:
        print(symbol,'WON')
        return True
    return False

def play():
    for turn in range(9):
        if turn%2==0:
            print('X turn')
            place(p1_symbol)
            if won(p1_symbol):
                break
        else:
            print('O turn')
            place(p2_symbol)
            if won(p2_symbol):
                break
    if not(won(p1_symbol)) and not(won(p2_symbol)):
        print('Draw')

play()
