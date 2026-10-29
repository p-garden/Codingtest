def solution(s):
    answer = len(s)
    for unit in range(1,len(s)//2+1):
        result =''
        prev = s[:unit]
        count=1
        
        for i in range(unit,len(s),unit):
            current = s[i:i+unit]
            
            if current == prev:
                count+=1
            else:
                if count >1:
                    result += str(count)
                result += prev
                prev = current
                count=1
            
        if count >1:
            result += str(count)
        result += current
        answer = min(answer,len(result))
    return answer