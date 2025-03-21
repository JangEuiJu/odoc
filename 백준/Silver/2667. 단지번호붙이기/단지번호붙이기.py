# 실행 단축키 shift + f11

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
result = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    q = deque()
    q.append([a, b])
    graph[a][b] = 0
    count = 1
    
    while q:
        x, y = q.popleft()
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= len(graph) or ny < 0 or ny >= len(graph):
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append([nx, ny])
                count += 1
                
    return count

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count = bfs(i, j)
            result.append(count)

result.sort()

print(len(result))  
for k in result:
    print(k)