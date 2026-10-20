def solution(m, n, board):
    answer = 0
    delete = True
    board = [list(row) for row in board]
        
    while delete:
        candidate = set()
        delete = False
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != ' ' and board[i][j] == board[i][j+1] ==board[i+1][j] ==board[i+1][j+1]:
                    candidate.add((i,j))
                    candidate.add((i,j+1))
                    candidate.add((i+1,j))
                    candidate.add((i+1,j+1))
                    
        if candidate:
            delete = True
            answer += len(candidate)
            for x,y in candidate:
                board[x][y]=' '

            for i in range(m-1):
                for j in range(m-1):
                    for k in range(n):
                        if board[j+1][k] ==' ':
                            board[j+1][k], board[j][k]= board[j][k],' '                        
    
    return answer