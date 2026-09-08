def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])
    
    parent = [m for m in range(n)]
    
    def find(a):
        if parent[a] == a:
            return a
        parent[a] = find(parent[a])
        return parent[a] 
    
    def union(a,b):
        a_parent = find(a)
        b_parent = find(b)
        if a_parent != b_parent:
            parent[b_parent]=a_parent    
    
    for a,b,cost in costs:
        a_parent = find(a)
        b_parent = find(b)
        if a_parent != b_parent:
            union(a,b)
            answer+= cost

    return answer