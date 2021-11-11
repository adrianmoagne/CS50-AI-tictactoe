"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    cont_x = 0
    cont_o = 0
    if not any(X or O in options for options in board):
        return X
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == X:
                    cont_x+=1
                if board[i][j] == O:
                    cont_o+=1
        if cont_x <= cont_o:
            return X
        else:
            return O
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action.add((i,j))
    return action
    


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    print(action)
    if action is None:
        raise Exception
    clone = copy.deepcopy(board)
    clone[action[0]][action[1]] = player(board)
    return clone
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i].count(X) == 3:
            return X
        if board[i].count(O) == 3:
            return O
        column = [row[i] for row in board]
        if column.count(X) == 3:
            return X
        if column.count(O) == 3:
            return O

        
    if board[1][1] is not EMPTY:
        if board[0][0] ==  board[1][1] ==  board[2][2]:
            return board[0][0]
        
        if board[0][2] == board[1][1] == board[2][0]:
            return board[0][2]
    
  
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if not any(EMPTY in options for options in board) or winner(board) is not None:
        return True
    
    return False

   


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) is not None:
            if winner(board) == X:
                return 1
            return -1
        return 0
    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    if player(board) == X:
        v ,action = max_value(board)
        return action
    else:
        v, action = min_value(board)
        return action 


def max_value(board):
    if terminal(board):
        return utility(board) , None
    v = - math.inf
    aux = v
    for action in actions(board):
        
        v , temp =  min_value(result(board,action))
        if v == 1:
            return v , action
        if v > aux :
            aux = v
            move = action
    return aux , move
        


def min_value(board):
    if terminal(board):
        return utility(board) , None
    v =  math.inf
    aux = v
    for action in actions(board):
        v , temp=  max_value(result(board,action))
        if v == -1:
            return v, action
        if v < aux :
            aux = v
            move = action

    return aux,move



