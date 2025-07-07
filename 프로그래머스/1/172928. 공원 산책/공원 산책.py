def solution(park, routes):
    H = len(park)
    W = len(park[0])

    # 방향 벡터
    move = {
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
        'E': (0, 1)
    }

    # 시작 위치 찾기
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                y, x = i, j
                break

    # 명령 수행
    for r in routes:
        d, n = r.split()
        dy, dx = move[d]
        n = int(n)

        ny, nx = y, x
        flag = True

        for _ in range(n):
            ny += dy
            nx += dx

            # 공원 벗어나면 취소
            if not (0 <= ny < H and 0 <= nx < W):
                flag = False
                break

            # 장애물 만나면 취소
            if park[ny][nx] == 'X':
                flag = False
                break

        # 이동 가능하면 위치 갱신
        if flag:
            y, x = ny, nx

    return [y, x]