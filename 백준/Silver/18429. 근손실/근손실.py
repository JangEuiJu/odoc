def find(x,n):
    global result
    if x < 500:
        return 
    if n == N: 
        result += 1 
        return 
    x -= K  
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            find(x + kit[i],n+1)
            visited[i] = 0

import sys
N, K = map(int, sys.stdin.readline().split())
kit = list(map(int,sys.stdin.readline().split()))
result = 0 
visited = [0]*N
find(500,0)
print(result)