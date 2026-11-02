def distance(hand_pos, target_pos):
    return abs(hand_pos[0] - target_pos[0]) + abs(hand_pos[1] - target_pos[1])
        
def solution(numbers, hand):
    keypad = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2),
    0: (3, 1), 
    }
    L= (3,0)
    R= (3,2)
    answer = ''
    for n in numbers:
        target = keypad[n]
        if n in [1, 4, 7]:
            answer += 'L'
            L = target

        elif n in [3, 6, 9]:
            answer += 'R'
            R = target
        else:
            L_D = distance(L,target)
            R_D = distance(R,target)
            if L_D == R_D:
                if hand =='right':
                    answer += 'R'
                    R = target
                else:
                    answer += 'L'
                    L = target
            elif L_D < R_D:
                answer += 'L'
                L = target
            else:
                answer += 'R'
                R = target
        
    return answer