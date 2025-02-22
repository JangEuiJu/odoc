from collections import deque
import sys, heapq

input = sys.stdin.readline 

n, m = map(int, input().split())
graph = [list(input().strip()) for i in range(n)]

def find_start():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == "I":
                return i, j

cnt = 0
r, c = find_start()
queue = deque([(r, c)])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[False] * m for _ in range(n)]
visited[r][c] = True

while queue:
    x, y = queue.popleft()
    for i in range (4): 
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] != "X":
            visited[nx][ny] = True
            if graph[nx][ny] == "P":
                cnt += 1
            queue.append((nx, ny))
              
print(cnt if cnt > 0 else "TT")