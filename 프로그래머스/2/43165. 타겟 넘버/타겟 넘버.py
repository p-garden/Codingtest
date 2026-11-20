def solution(numbers, target):
    answer = 0
    def dfs(index, total):
        if index == len(numbers):
            if target == total:
                return 1
            return 0
        plus = dfs(index+1, total+numbers[index])
        minus = dfs(index+1, total-numbers[index])
        return plus+minus
    return dfs(0,0)