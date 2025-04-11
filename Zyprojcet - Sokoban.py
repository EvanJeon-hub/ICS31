from game_settings import *
from copy import deepcopy
orig = deepcopy(board)

#finding location for sprite
def find_sprite(board):
    for g in range(len(board)):
        for h in range(len(board[0])):
            if board[g][h] in [SPRITE, SPRITE_T]:
                return g, h
    return None, None
i, j = find_sprite(board)

#printing
def printboard(board, spacing = True):
    for f in board:
        print(' '.join(f))
    if spacing == True:
        pass
    
# winning
def win(board):
    for h in board:
        if BOX_NS in h:
            return False
    return True

#moving sprite
def move_sprite(board, direct):
    global i, j
    row, col = i, j
    if direct == 'w':
        row -= 1
    elif direct == 'a':
        col -= 1
    elif direct == 's':
        row += 1
    elif direct == 'd':
        col += 1
    if 0 <= row < len(board) and 0 <= col < len(board[0]):
        if board[row][col] == EMPTY:
            board[i][j] = TARGET if board[i][j] == SPRITE_T else EMPTY
            board[row][col] = SPRITE
            i, j = row, col
        elif board[row][col] == TARGET:
            board[i][j] = TARGET if board[i][j] == SPRITE_T else EMPTY
            board[row][col] = SPRITE_T
            i, j = row, col
        elif board[row][col] in [BOX_NS, BOX_S]:
            brow, bcol = row, col
            if direct == 'w':
                brow -= 1
            elif direct == 'a':
                bcol -= 1
            elif direct == 's':
                brow += 1
            elif direct == 'd':
                bcol += 1
            if 0 <= brow < len(board) and 0 <= bcol < len(board[0]) and board[brow][bcol] in [EMPTY, TARGET]:
                board[brow][bcol] = BOX_S if board[brow][bcol] == TARGET else BOX_NS
                board[row][col] = SPRITE_T if board[row][col] == BOX_S else SPRITE
                board[i][j] = TARGET if board[i][j] == SPRITE_T else EMPTY
                i, j = row, col
                
#reset
def reset(s = None, l = None):
    global orig, board, i, j
    if s and l:
        board = deepcopy(s)
        orig = deepcopy(s)
        i, j = find_sprite(board)
    else:
        board = deepcopy(orig)
        i, j = find_sprite(board)
        
#outputs
def playgame():
    printboard(board)
    print()
    while True:
        move_spri = input()
        if move_spri == 'q':
            print('Goodbye')
            break
        elif move_spri == RESTART:
            reset()
            printboard(board)
            print()
        elif move_spri in CONTROLS:
            move_sprite(board, move_spri)
            printboard(board)
            if win(board):
                print('You Win!')
                break
            print()
        else:
            print('enter a valid move:')
reset() 
playgame()
