from collections import deque
import sys, heapq

input = sys.stdin.readline 

n, m = map(int, input().split())
board = list(range(101))

for _ in range(n):
    x, y = map(int, input().split())
    board[x] = y
for _ in range(m):
    u, v = map(int, input().split())
    board[u] = v

queue = deque([(1, 0)])
visited = [False] * 101
visited[1] = True

while queue:
    pos, count = queue.popleft()
    if pos == 100:
        print(count)
        break
    for i in range(1, 7):
        next_pos = pos + i
        if next_pos <= 100 and not visited[next_pos]:
            visited[next_pos] = True
            queue.append((board[next_pos], count+1))