def solution(routes):
    answer = 0
    routes.sort(key=lambda x :x[1])
    camera= -30001
    for enter,exit in routes:
        if enter > camera:
            camera = exit
            answer += 1
    return answer