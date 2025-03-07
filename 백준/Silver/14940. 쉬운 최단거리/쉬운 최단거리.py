from collections import deque
import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 0
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if arr[nx][ny] == 0:
                    visited[nx][ny] = 0
                elif arr[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny)) 
                    
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2 and visited[i][j] == -1:
            bfs(i, j)
            
            
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()