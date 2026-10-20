def solution(places):
    answer = []
    
    for room in places:
        district = False
        for i,row in enumerate(room):
            for j,char in enumerate(row):
                if district: 
                    continue
                if room[i][j] =='P':
                    if (j+1 < len(room[i]) and room[i][j+1] == 'P' or 
                            i+1 < len(room) and room[i+1][j] == 'P' or 
                            ((j+1 < len(room[i]) and i+1 < len(room)) and room[i+1][j+1] == 'P' and (room[i][j+1] =='O' or room[i+1][j] =='O')) or 
                            ((j+1 < len(room[i]) and i-1 >= 0) and room[i-1][j+1] == 'P' and (room[i][j+1] =='O' or room[i-1][j] =='O')) or 
                            (j + 2 < len(room[i]) and room[i][j+2]=='P' and  room[i][j+1] =='O') or 
                            (i + 2 < len(room) and room[i+2][j]=='P' and  room[i+1][j] =='O')):
                        district = True
        if district:
            answer.append(0)
        else:
            answer.append(1)
            
    return answer