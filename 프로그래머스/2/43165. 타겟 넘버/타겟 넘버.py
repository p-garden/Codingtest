def solution(numbers, target):
    answer = 0

    def dfs(pos, total):
        if pos == len(numbers):
            if total == target:
                return 1
            else:
                return 0
        plus = dfs(pos+1,total + numbers[pos])
        minus = dfs(pos+1, total -numbers[pos])
        return plus+minus
    return dfs(0,0)