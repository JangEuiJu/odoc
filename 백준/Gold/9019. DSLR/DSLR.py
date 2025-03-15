# 실행 단축키 shift + f11

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    visited = [False for i in range(10001)]
    q = deque()
    q.append([a,''])
    visited[a] = True
    
    while q:
        num, oper = q.popleft()
        if num == b:
            print(oper)
            break
        
        d = num * 2 % 10000
        if not visited[d]:
            visited[d] = True
            q.append([d, oper + "D"])
            
        s = (num - 1) % 10000
        if not visited[s]:
            visited[s] = True
            q.append([s, oper + "S"])
            
        l = num // 1000 + (num % 1000)*10
        if not visited[l]:
            visited[l] = True
            q.append([l, oper + 'L'])

        r = num // 10 + (num % 10) * 1000
        if not visited[r]:
            visited[r] = True
            q.append([r, oper + 'R'])
    