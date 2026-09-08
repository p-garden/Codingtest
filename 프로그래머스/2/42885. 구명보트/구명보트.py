def solution(people, limit):
    #people을 정렬후 투포인터를 이용해서 남은 무게를 반대편에서 탐색 O(n logn)
    answer = 0
    people.sort()
    left = 0
    right = len(people)-1
    
    while left <= right:
        if limit >= people[left] + people[right]:
            answer += 1
            left+=1
            right-=1    
        else:
            answer+=1
            right-=1
            
    return answer