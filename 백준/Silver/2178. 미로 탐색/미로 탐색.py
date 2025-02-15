from collections import deque
import sys

input = sys.stdin.readline 

n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(a, b):
    q = deque()
    q.append((a, b))
    arr[a][b] = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m :
                if arr[nx][ny] == "1" :
                    q.append((nx, ny))
                    arr[nx][ny] = arr[x][y] + 1
    return arr[n-1][m-1]

print(bfs(0,0))

