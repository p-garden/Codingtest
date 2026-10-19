def solution(rows, columns, queries):
    matrix = [ [i*columns+j+1 for j in range(columns)] for i in range(rows)]
    answer = []
    
    
    for x1,y1,x2,y2 in queries:
        x1-=1
        x2-=1
        y1-=1
        y2-=1
        pre = matrix[x1][y1]
        min_value = pre
        for x in range(x1,x2):
            matrix[x][y1] =  matrix[x+1][y1] 
            min_value=min(min_value,matrix[x][y1])
        for y in range(y1,y2):
            matrix[x2][y] = matrix[x2][y+1]
            min_value=min(min_value,matrix[x2][y])
        for x in range(x2,x1,-1):
            matrix[x][y2] =  matrix[x-1][y2]
            min_value=min(min_value,matrix[x][y2])
        for y in range(y2,y1,-1):
            matrix[x1][y] = matrix[x1][y-1]
            min_value=min(min_value,matrix[x1][y])
        matrix[x1][y1+1] = pre
        answer.append(min_value)
        
    return answer