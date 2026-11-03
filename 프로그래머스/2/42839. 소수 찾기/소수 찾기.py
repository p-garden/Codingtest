from itertools import permutations
import math
def solution(numbers):
    answer = 0
    num = set()
    for i in range(1,len(numbers)+1):
        for p in permutations(numbers,i):
            num.add(int(''.join(p)))
    print(num)
    
    for n in num:
        if n < 2:
            continue
            
        for i in range(2,int(math.sqrt(n))+1):
            if n % i ==0:
                break
        else:
            answer+=1
                
    return answer