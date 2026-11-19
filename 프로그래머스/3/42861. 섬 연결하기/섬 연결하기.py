

def solution(n, costs):
    def find(a):
        if a ==parent[a]:
            return a
        return find(parent[a])

    def union(a,b):
        if find(a) != find(b):
            parent[find(b)] = parent[find(a)]
            
    answer = 0
    costs.sort(key= lambda x:x[2])
    parent = [i for i in range(n)]
    
    for a,b,c in costs:
        if find(a) != find(b):
            union(a,b)
            answer+=c
    return answer