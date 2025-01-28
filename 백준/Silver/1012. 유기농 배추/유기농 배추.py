from collections import deque

import sys
input = sys.stdin.readline

def bfs(x, y):
    queue = deque([(x, y)])
    matrix[x][y] = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if matrix[nx][ny] == 1:
                queue.append((nx, ny))
                matrix[nx][ny] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    matrix = [[0]*(n) for _ in range(m)]
    count = 0
    
    for i in range(k):
        x, y = map(int, input().split())
        matrix[x][y] = 1
        
    for x in range(m):
        for y in range(n):
            if matrix[x][y] == 1:
                bfs(x, y)
                count += 1

    print(count)
        