def solution(new_id):
    #1단계
    new_id = new_id.lower()
    
    #2단계
    result = []
    for character in new_id:
        if character.isalpha() or character.isdigit() or character in '-_.': 
            result.append(character)
    new_id = ''.join(result)
    
    #3단계
    result = []
    for character in new_id:
        if character == '.' and result and result[-1] =='.':
            continue
        result.append(character)
    new_id = ''.join(result)
    
    #4단계
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]

    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]
        
    #5단계
    if not new_id:
        new_id = "a"
    
    #6단계
    if len(new_id) >=16:
        new_id = new_id[:15]
        
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]
    
    #7단계
    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id