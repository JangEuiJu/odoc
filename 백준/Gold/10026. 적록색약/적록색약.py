# 실행 단축키 shift + f11

from collections import deque
import sys, heapq
input = sys.stdin.readline

n = int(input())
arr = [list(input().strip()) for i in range(n)]
q = deque()

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    q.append((x, y))
    visited[x][y] = True
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == arr[x][y] and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
    

# 적록색약 아닌 경우
visited = [[False]* n for i in range(n)]
count1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            count1 += 1


# 적록색약
for i in range(n):
    for j in range(n):
        if arr[i][j] == "G":
            arr[i][j] = "R"
visited = [[False]* n for i in range(n)]
count2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            count2 += 1


print(count1, count2)