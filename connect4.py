#!/usr/bin/env python3

def print_board(board):
    print('       0     1     2     3     4     5     6')
    for i in range(len(board)):
        print()
        print()
        print(f'    |',end='  ')
        for j in range(len(board[i])):
            print(f'{board[i][j]}  |  ',end='')
            
def valid_entry(board,input):
    validity=False
    if input < 0 or input >= len(board):
        print('Not valid entry')
        print()
    else: validity=True
    return validity
def drop_down(col,board):
    lowest=-1
    for i in range(len(board)): 
        if board[i][col]== 0:
            lowest=i
    if lowest== -1:
        print()
        print('Cannot drop piece here')
    return lowest 
   
   #-----------------------------------------------------------------     
def check_win(row,col,board,player_num):
    #winner=-1
    counter=0
    #rown
    for i in range(len(board)):
        if board[i][col] ==player_num:
            counter+=1
        else: counter=0
        if counter==4: return player_num
        
    #column
    counter=0
    for b in range(len(board[0])):
        if board[row][b] ==player_num:
            counter+=1
        else: counter=0
        if counter==4: return player_num
        
    #diagonal down left from top
    counter=0
    c=min(row,(len(board[0])-col-1))
    new_col=col+c
    new_row=row-c
    limit=min( new_col, len(board)-new_row-1)
    if limit==6:limit=5
    for d in range(limit+1):
        if board[new_row+d][new_col-d] ==player_num:
            counter+=1
        else: counter=0
        if counter==4: return player_num
        
    #diagonal down right from top
    counter=0
    c=min(row,col)
    new_col=col-c
    new_row=row-c
    limit=min( len(board[0])-new_col-1 , len(board)-new_row -1)
    if limit==6:limit=5
    for d in range(limit+1):
        if board[new_row+d][new_col+d] ==player_num:
            counter+=1
        else: counter=0
        if counter==4: return player_num
        
    return -1
#----------------------------------------------------------------------------

def check_tie(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 0: return False
    return True
            
            


               
board=[[0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]]
      
            
game_over = False
player_turn = 1


while not game_over:
    print_board(board)
    print()
    print()
    valid_input=False
    while valid_input==False:
        while True:
            try:
                col_selected=int(input(f'Player {player_turn} : Enter column number :  '))
                break
            except ValueError:
                print("""
Please Enter a Number
                """,flush=True)
        if col_selected >= 0 and col_selected < 7:
            row=drop_down(col_selected,board)
            if row==-1:
                continue
        valid_input=valid_entry(board[0],col_selected)
    
    print()
    board[row][col_selected] = player_turn
    if check_win(row,col_selected,board,player_turn) != -1:
        print()
        print_board(board)
        print(f"""
PLAYER  {player_turn}   WINS!!!""")
        game_over=True
        
    if check_tie(board) ==True:
        print()
        print_board(board)
        print(f"""
TIE GAME""")
        game_over=True
        
    if player_turn == 1:
        player_turn = 2
    else:
        player_turn = 1
            
            
        
    








