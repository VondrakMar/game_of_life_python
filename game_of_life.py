import numpy as np
import sys

def move_cursor_up(n):
    sys.stdout.write(f"\033[{n}A")

def clear_line():
    sys.stdout.write("\033[K")


def rules(state,neighs):
    if state == 1:
        # under population
        if neighs < 2:
            return 0
        elif neighs > 3:
            return 0
        else:
            return 1
    elif state == 0:
        if neighs == 3:
            return 1
        else:
            return 0

def count_neighs(pos_x,pos_y,board):
    count_neighs = 0
    directions = [-1,0,1]
    for dx in directions:
        for dy in directions:
            if dx == 0 and dy == 0:
                continue
            row_neig = pos_x + dx
            col_neig = pos_y + dy
            if row_neig > board.shape[0]-1:
                row_neig = 0
            elif row_neig < 0:
                row_neig = board.shape[0]-1
            if col_neig > board.shape[1]-1:
                col_neig = 0
            elif col_neig < 0:
                col_neig = board.shape[1]-1
            count_neighs += board[row_neig,col_neig]
    return count_neighs

def print_board(board):
    print("############################")
    for row in board:
        for field in row:
            print(int(field),end=" ",)
        print("")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

def read_map():
    f = open("life_map.txt","r").readlines()
    board_map = []
    for line in f:
        row = []
        line = line.split()
        for n in line:
            row.append(int(n))
        board_map.append(row)

    return (np.array(board_map))

life_board = read_map()
print_board(life_board)
for iteration in range(100):
    old_board = life_board.copy()
    life_board = np.zeros_like(life_board)
    for id_x,row in enumerate(old_board):
        for id_y,n in enumerate(row):
            neighs = count_neighs(id_x,id_y,old_board)
            life_board[id_x,id_y] = rules(old_board[id_x,id_y],neighs)
    print_board(life_board)
            

