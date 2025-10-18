def solution(array, commands):
    answer = []
    print(len(commands))
    #for n in range(len(commands):
    for i,j,k in commands:
        arr = array[i-1:j]
        arr.sort()
        l = arr[k-1]
        answer.append(l)
    return answer