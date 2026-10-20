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

            for y in range(n):
                col = [board[x][y] for x in range(m) if board[x][y] != ' ']

                for x in range(m - 1, -1, -1):
                    if col:
                        board[x][y] = col.pop()
                    else:
                        board[x][y] = ' '    
    
    return answer