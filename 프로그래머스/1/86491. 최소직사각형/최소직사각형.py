def solution(sizes):
    answer = 0
    for size in sizes:
        size.sort()
    min_max=sizes[0][0]
    max_max=sizes[0][1]
    for min_,max_ in sizes:
        max_max = max(max_,max_max)
        min_max = max(min_,min_max)
    answer = max_max*min_max
    return answer