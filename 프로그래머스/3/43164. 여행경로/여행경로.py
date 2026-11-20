def solution(tickets):
    answer=[]
    visited = [False] * len(tickets) 
    def dfs(start, path, dist):
        if dist == len(tickets):
            answer.append(path[:])
            return
        
        for i in range(len(tickets)):
            if not visited[i] and tickets[i][0] == start:
                visited[i] = True
                path.append(tickets[i][1])
                dfs(tickets[i][1],path,dist+1)
                
                path.pop()
                visited[i]=False
                
                
    dfs("ICN", ["ICN"], 0)
    answer.sort()
    return answer[0] if answer else []