# #실행 단축키 shift + f11

import sys
input = sys.stdin.readline 

t = int(input())

def valid_sudoku(board):
    for row in board:
        if sorted(row) != list(range(1, 10)):
            return False
        
    for col in range(9):
        if sorted([board[row][col] for row in range(9)]) != list(range(1, 10)):
            return False
    
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            block = []
            for i in range(3):
                for j in range(3):
                    block.append(board[box_row + i][box_col + j])
            if sorted(block) != list(range(1, 10)):
                return False
    
    return True

i = 0
while i < t:
    board = []
    while len(board) < 9:
        line = input().strip()
        if line == "":
            continue 
        board.append(list(map(int, line.split())))
    
    result = valid_sudoku(board)
    if result:
        print(f"Case {i+1}: CORRECT")
    else:
        print(f"Case {i+1}: INCORRECT")
    i += 1
