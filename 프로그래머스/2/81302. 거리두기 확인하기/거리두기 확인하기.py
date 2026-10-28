def solution(places):
    answer = []

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for place in places:
        valid = 1

        for i in range(5):
            for j in range(5):
                if place[i][j] != 'P':
                    continue

                # 거리 1 검사
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy

                    if 0 <= nx < 5 and 0 <= ny < 5:
                        if place[nx][ny] == 'P':
                            valid = 0

                # 거리 2 검사: 같은 행 또는 같은 열
                for dx, dy in [(2, 0), (-2, 0),
                               (0, 2), (0, -2)]:
                    nx, ny = i + dx, j + dy
                    mx, my = i + dx // 2, j + dy // 2

                    if 0 <= nx < 5 and 0 <= ny < 5:
                        if (place[nx][ny] == 'P'
                                and place[mx][my] != 'X'):
                            valid = 0

                # 대각선 거리 2 검사
                for dx, dy in [(1, 1), (1, -1),
                               (-1, 1), (-1, -1)]:
                    nx, ny = i + dx, j + dy

                    if 0 <= nx < 5 and 0 <= ny < 5:
                        if place[nx][ny] == 'P':
                            if (place[i][ny] != 'X'
                                    or place[nx][j] != 'X'):
                                valid = 0

        answer.append(valid)

    return answer