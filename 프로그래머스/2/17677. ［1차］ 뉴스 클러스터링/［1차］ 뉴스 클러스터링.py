def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()

    arr1 = []
    arr2 = []
    for i in range(len(str1) - 1):
        temp = str1[i:i+2]
        if temp.isalpha():
            arr1.append(temp)

    for i in range(len(str2) - 1):
        temp = str2[i:i+2]
        if temp.isalpha():
            arr2.append(temp)
    print(arr1,arr2)
    interaction=0
    
    temp = arr2.copy()
    for i in arr1:
        if i in temp:
            interaction += 1
            temp.remove(i)  
            
    union = len(arr1) + len(arr2) - interaction
    if union ==0:
        union =1
        interaction=1
    answer = (interaction / union) * 65536 //1
        
    return answer