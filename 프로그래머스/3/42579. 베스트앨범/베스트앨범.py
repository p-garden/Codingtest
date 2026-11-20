def solution(genres, plays):
    answer=[]
    pos=0
    s_plays=[]
    for i in range(len(plays)):
        s_plays.append((plays[i],genres[i],pos))
        pos+=1
    s_plays.sort(key=lambda x:x[0], reverse=True)

    rank = dict()
    for i in range(len(genres)):
        rank[genres[i]] = rank.get(genres[i],0)+plays[i]
    rank = dict(sorted(rank.items(), key=lambda x:x[1], reverse=True))
    
    
    for genre in rank.keys():
        local_cnt=0
        for i in range(len(s_plays)):
            if local_cnt ==2:
                break
            if genre == s_plays[i][1]:
                answer.append(s_plays[i][2])
                local_cnt+=1
    return answer