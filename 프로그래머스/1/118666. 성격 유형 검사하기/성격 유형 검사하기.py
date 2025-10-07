def solution(survey, choices):
    scores = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    indicators = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    for s, c in zip(survey, choices):
        
        diff = c - 4
        
        if diff < 0:
            scores[s[0]] += abs(diff)
        elif diff > 0:
            scores[s[1]] += diff
    
    answer = ''
    for type1, type2 in indicators:
        if scores[type1] >= scores[type2]:
            answer += type1
        else:
            answer += type2
    return answer