def solution(numbers, target):
    def dsf(index,total):
        if index == len(numbers):
            if total == target:
                return 1
            return 0
        plus = dsf(index+1, total+numbers[index])
        minus = dsf(index+1, total-numbers[index])
        return plus+minus
    
    return dsf(0,0)