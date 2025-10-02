def solution(friends, gifts):
    answer = 0
    n = len(friends)
    name_to_index = {name: i for i, name in enumerate(friends)}
    gift_matrix =[[0] * n for _ in range(n)]
    gift_index = [0] * n
    
    for gift in gifts:
        giv,rec = gift.split()
        giver_idx = name_to_index[giv]
        receiver_idx = name_to_index[rec]
        
        gift_matrix[giver_idx][receiver_idx] += 1

    for i in range(n):
        give_sum = sum(gift_matrix[i])
        receive_sum = 0
        for j in range(n):
            receive_sum += gift_matrix[j][i]
        gift_index[i] = give_sum-receive_sum     
    
    fin = [0] * n
    for i in range(n):
        tmp =0
        for j in range(n):
            if (gift_matrix[i][j] > gift_matrix[j][i]):
                tmp +=1
            elif (gift_matrix[i][j] == gift_matrix[j][i]) or (gift_matrix[i][j] == 0 and gift_matrix[j][i] == 0):
                if gift_index[i] > gift_index[j]:
                    tmp +=1
        fin[i] = tmp
    answer = max(fin)
    return answer
