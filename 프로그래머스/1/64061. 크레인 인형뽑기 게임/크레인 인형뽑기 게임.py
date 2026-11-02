def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        for j in range(len(board)):
            if board[j][move-1] != 0:
                if len(stack) !=0 and board[j][move-1] == stack[-1]:
                    stack.pop()
                    answer+=2
                else:
                    stack.append(board[j][move-1])
                board[j][move-1] = 0
                break
            
                
    return answer