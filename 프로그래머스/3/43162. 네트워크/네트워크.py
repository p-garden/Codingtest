def solution(n, computers):
    parent = [m for m in range(n)]
    answer = 0
    def find(a):
        if a == parent[a]:
            return a
        return find(parent[a])
    
    def union(a,b):
        if find(a) != find(b):
            parent[find(b)] = parent[find(a)]
            
    for i in range(n):
        for j in range(i+1,n):
            if computers[i][j] == 1 and find(i) != find(j):
                union(i,j)

    parent = set([find(i) for i in parent])
                 
    answer = len(parent)
    
        
    return answer
