def solution(participant, completion):
    people = dict()
    for p in participant:
        people[p] = people.get(p,0)+1
    for c in completion:
        people[c] -=1
    for name,cnt in people.items():
        if cnt>0:
            return name
