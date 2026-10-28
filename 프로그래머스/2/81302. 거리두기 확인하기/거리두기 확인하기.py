def solution(places):
    answer = []
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    
    for place in places:
        valid =1
        for i in range(5):
            for j in range(5):
                if place[i][j] != 'P':
                    continue
                for dx,dy in directions:
                    nx,ny = i+dx,j+dy
                    if 0<= nx <5 and 0<=ny<5 and place[nx][ny] =='P':
                        valid=0
                
                for dx,dy in [(0,2),(2,0),(0,-2),(-2,0)]:
                    nx,ny = i+dx,j+dy
                    mx,my = i+dx//2,j+dy//2
                    if 0<= nx <5 and 0<=ny<5:
                        if place[nx][ny] =='P' and place[mx][my] !='X':
                            valid=0
                            
                for dx,dy in [(-1,1),(1,1),(1,-1),(-1,-1)]:
                    nx,ny = i+dx,j+dy
                    if 0<= nx <5 and 0<=ny<5:
                        if place[nx][ny] =='P'and (place[i][ny] !='X'or place[nx][j]!='X'):
                            valid=0
        answer.append(valid)
    return answer