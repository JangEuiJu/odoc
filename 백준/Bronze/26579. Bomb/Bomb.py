import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    r, c = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(r)]

    up = [[0]*c for _ in range(r)]
    down = [[0]*c for _ in range(r)]
    left = [[0]*c for _ in range(r)]
    right = [[0]*c for _ in range(r)]

    # 위쪽 누적
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '#':
                up[i][j] = 0
            else:
                up[i][j] = (up[i-1][j] if i > 0 else 0) + (1 if grid[i][j] == '@' else 0)

    # 아래쪽 누적
    for i in range(r-1, -1, -1):
        for j in range(c):
            if grid[i][j] == '#':
                down[i][j] = 0
            else:
                down[i][j] = (down[i+1][j] if i < r-1 else 0) + (1 if grid[i][j] == '@' else 0)

    # 왼쪽 누적
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '#':
                left[i][j] = 0
            else:
                left[i][j] = (left[i][j-1] if j > 0 else 0) + (1 if grid[i][j] == '@' else 0)

    # 오른쪽 누적
    for i in range(r):
        for j in range(c-1, -1, -1):
            if grid[i][j] == '#':
                right[i][j] = 0
            else:
                right[i][j] = (right[i][j+1] if j < c-1 else 0) + (1 if grid[i][j] == '@' else 0)

    best_r, best_c, best_cnt = 0, 0, -1

    for i in range(r):
        for j in range(c):
            if grid[i][j] == '.':
                # 현재 칸 포함 안 함
                kills = (up[i-1][j] if i > 0 else 0) \
                        + (down[i+1][j] if i < r-1 else 0) \
                        + (left[i][j-1] if j > 0 else 0) \
                        + (right[i][j+1] if j < c-1 else 0)
                if kills > best_cnt:
                    best_cnt = kills
                    best_r, best_c = i, j

    print(f"{best_r}, {best_c}")
