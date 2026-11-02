def solution(fees, records):
    answer = []
    car_time = dict()
    car_stats = dict()
    
    for record in records:
        time, car, status = record.split()
        h, m = map(int, time.split(':'))
        minutes = h * 60 + m
        
        if status == 'IN':
            car_stats[car] = minutes
            if car not in car_time:
                car_time[car] = 0
        else:
            time_diff = minutes - car_stats[car]
            car_time[car] += time_diff
            del car_stats[car]
            
    for c, t in car_stats.items():
        minutes = 23* 60+59
        time_diff = minutes - t
        car_time[c] += time_diff
    
    for c,t in sorted(car_time.items()):
        if t <= fees[0]:
            price = fees[1]
        else:
            remain_time = t - fees[0]
            price = fees[1] + ((remain_time+fees[2]-1) // fees[2]) * fees[3]
        answer.append(price)
    
    return answer