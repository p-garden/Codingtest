def solution(n, stations, w):
    answer = 0
    prev=1
    impact = 2*w+1
    for station in stations:
        first = max(station-w,1)
        last = min(station+w,n)
        remain = first - prev
        if remain > 0:
            answer += (remain+impact-1) // impact
        prev = last+1
    remain = n-prev+1
    if remain>0:
        answer += (remain+impact-1) // impact

    return answer
