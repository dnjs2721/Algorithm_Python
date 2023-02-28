def check(board, mark):
        if (board[0][0] == mark and board[0][1] == mark and board[0][2] == mark) or \
            (board[1][0] == mark and board[1][1] == mark and board[1][2] == mark) or \
            (board[2][0] == mark and board[2][1] == mark and board[2][2] == mark) or \
            (board[0][0] == mark and board[1][0] == mark and board[2][0] == mark) or \
            (board[0][1] == mark and board[1][1] == mark and board[2][1] == mark) or \
            (board[0][2] == mark and board[1][2] == mark and board[2][2] == mark) or \
            (board[0][0] == mark and board[1][1] == mark and board[2][2] == mark) or \
            (board[0][2] == mark and board[1][1] == mark and board[2][0] == mark):
                return True
        else:
            return False

def solution(board):
    o_count = 0
    x_count = 0
        
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                o_count += 1
            elif board[i][j] == 'X':
                x_count += 1
            
    o_win = check(board, 'O')
    x_win = check(board, 'X')        
            
    if o_win and x_win:
         return 0    
    elif o_win:
        if o_count - x_count == 1:
            return 1
        else:
            return 0
    elif x_win:
        if o_count == x_count:
            return 1
        else:
            return 0
    
    if o_count == 0 and x_count > 0:
        return 0
    elif o_count < x_count:
        return 0
    elif o_count - x_count > 1:
        return 0
    
    return 1

print(solution(["XOO", ".O.", "..."]))