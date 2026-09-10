def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    prev= -30001
    for enter,exit in routes:
        if enter>prev:
            prev =exit
            answer+=1
    return answer