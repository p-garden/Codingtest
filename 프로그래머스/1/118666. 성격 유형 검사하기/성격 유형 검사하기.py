def solution(survey, choices):
    answer = ''
    answer_list = [0] * 4

    sample = [['R','T'],['C','F'],['J','M'],['A','N']]
    
    for i in range(len(survey)):
        if 'R' in survey[i]:
            if survey[i][1] == 'R':
                answer_list[0] += choices[i] - 4
            else: 
                answer_list[0] += -(choices[i] - 4)
        if 'C' in survey[i]:
            if survey[i][1] == 'C':
                answer_list[1]  += choices[i] - 4
            else: 
                answer_list[1]  += -(choices[i] - 4)
        if 'J' in survey[i]:
            if survey[i][1] == 'J':
                answer_list[2]  += choices[i] - 4
            else: 
                answer_list[2]  += -(choices[i] - 4)
        if 'A' in survey[i]:
            if survey[i][1] == 'A':
                answer_list[3]  += choices[i] - 4
            else: 
                answer_list[3]  += -(choices[i] - 4)
    
    for tmp in range(4):
        if answer_list[tmp] >=0:
            answer+=(sample[tmp][0])
        else:
            answer+=(sample[tmp][1])
    return answer