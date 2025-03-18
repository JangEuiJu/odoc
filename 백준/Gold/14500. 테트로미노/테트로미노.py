# 실행 단축키 shift + f11

import sys
from collections import deque
input = sys.stdin.readline

allCases = [[(0,1), (0,2), (0,3)], [(1,0), (2,0), (3,0)], 
        [(0,1), (1,0), (1,1)], 
        [(1,0),(1,1),(2,1)], [(0,-1), (1,-1), (1,-2)], 
        [(1,0), (1,-1), (2,-1)],[(0,1), (1,1), (1,2)],
        [(1,0), (2,0), (2,1)], [(0,1), (0,2), (1,0)], 
        [(0,1),(1,1), (2,1)], [(0,1), (0,2), (-1,2)],
        [(1,0),(2,0),(2,-1)],[(0,1),(0,2),(1,2)], 
        [(1,0),(2,0),(0,1)], [(1,0),(1,1),(1,2)],
        [(1,0),(1,1),(1,-1)], [(1,0),(1,1),(2,0)],
        [(0,-1),(1,0),(0,1)],[(0,1),(-1,1),(1,1)] 
]

def calc(i, j, case):
    temp = arr[i][j]
    for di, dj in case:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m:
            temp += arr[ni][nj]
        else : 
            return 0
    return temp

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

res = 0
for i in range(n):
    for j in range(m):
        for case in allCases:
            temp = calc(i, j, case)
            res = max(res, temp)

print(res)