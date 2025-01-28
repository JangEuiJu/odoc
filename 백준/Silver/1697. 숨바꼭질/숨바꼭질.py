from collections import deque

import sys
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(count[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 100000 and not count[nx]:
                count[nx] = count[x] + 1
                q.append(nx)

n, k = map(int, input().split())
count = [0] * (100000 + 1)

bfs()