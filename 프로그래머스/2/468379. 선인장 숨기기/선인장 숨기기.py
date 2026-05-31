from collections import deque

def solution(m, n, h, w, drops):
    # 1. 각 격자 칸이 몇 번째 빗방울에 젖는지 기록 (1부터 시작)
    # 비를 맞지 않는 칸은 무한대(inf)로 초기화
    INF = float('inf')
    grid = [[INF] * n for _ in range(m)]
    
    for i, (r, c) in enumerate(drops):
        grid[r][c] = i + 1

    # 2. 행(Row) 방향으로 크기 w의 윈도우 최솟값 구하기
    # row_min[r][c]는 grid[r][c]부터 grid[r][c+w-1]까지 중 최솟값
    row_min = [[0] * (n - w + 1) for _ in range(m)]
    
    for r in range(m):
        q = deque()
        for c in range(n):
            # 범위를 벗어난 인덱스 제거
            if q and q[0] < c - w + 1:
                q.popleft()
            # 현재 값보다 큰 이전 값들은 최솟값 후보에서 제외
            while q and grid[r][q[-1]] >= grid[r][c]:
                q.pop()
            q.append(c)
            
            # 윈도우 크기 w를 채운 시점부터 기록
            if c >= w - 1:
                row_min[r][c - w + 1] = grid[r][q[0]]

    # 3. 열(Column) 방향으로 크기 h의 윈도우 최솟값 구하기
    # row_min의 결과를 바탕으로 세로 방향 최솟값을 구하면, 최종적으로 h x w 영역의 최솟값이 됨
    best_time = -1
    ans_r, ans_c = -1, -1

    for c in range(n - w + 1):
        q = deque()
        for r in range(m):
            if q and q[0] < r - h + 1:
                q.popleft()
            while q and row_min[q[-1]][c] >= row_min[r][c]:
                q.pop()
            q.append(r)
            
            if r >= h - 1:
                current_min_time = row_min[q[0]][c]
                current_r = r - h + 1
                current_c = c
                
                # 조건 비교: 
                # 1. 더 늦게 비를 맞는 구역을 찾았을 때 (INF 포함)
                # 2. 동일하게 늦게 맞는다면, '가장 위쪽 행, 가장 왼쪽 열'은 루프 진행 순서(r 증가 후 c 증가) 상 
                #    최초에 발견된 것이 자동으로 최선이 되므로 strict 부등호(>) 사용
                if current_min_time > best_time:
                    best_time = current_min_time
                    ans_r = current_r
                    ans_c = current_c

    return [ans_r, ans_c]