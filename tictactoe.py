#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os

def clear_output():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

        
def display_board(board):
    clear_output()
    print('   |   |')
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('-----------')
    print('   |   |')
    print(' '+board[4]+' | '+board[5]+' | '+board[6])
    print('-----------')
    print('   |   |')
    print(' '+board[1]+' | '+board[2]+' | '+board[3])


# In[2]:


test_board=['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# In[5]:


def player_input():
    marker= ' '
    while marker !='X' and marker !='O':
        marker=input('Please choose your marker(X,O): ') .upper()
    if marker == 'X':
            return ('X','O')
    else:
            return ('O','X')


# In[9]:


player_input()


# In[11]:


def place_marker(board,marker,position):
    board[position]=marker


# In[13]:


place_marker(test_board,'$',8)
display_board(test_board)


# In[15]:


def win_check(board,mark):
    return ((board[7]==mark and board[8]==mark and board[9]==mark) or
            (board[4]==mark and board[5]==mark and board[6]==mark) or
            (board[1]==mark and board[2]==mark and board[3]==mark) or
            (board[7]==mark and board[4]==mark and board[1]==mark) or
            (board[8]==mark and board[5]==mark and board[2]==mark) or
            (board[9]==mark and board[6]==mark and board[3]==mark) or
            (board[7]==mark and board[5]==mark and board[3]==mark) or
            (board[9]==mark and board[5]==mark and board[1]==mark))


# In[17]:


win_check(test_board,'X')


# In[19]:


import random
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# In[21]:


def space_check(board,position):
    if board[position]==' ' :
        return True
    else:
        pass


# In[23]:


def full_board_check(board):
    if board=='X' or board=='O':
        return True
    else:
        return False


# In[25]:


def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position


# In[27]:


def replay():
    play= input("Do you want to play again?'yes' or 'no': ").lower()
    if play== 'yes':
        return True
    else:
        pass


# In[ ]:


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + 'will go first')
    
    play_game = input('Are you ready to play? yes or no.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
    


# In[ ]:




