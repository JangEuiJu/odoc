# 실행 단축키 shift + f11

import sys
from collections import deque
input = sys.stdin.readline

def lcs (a:str, b: str) -> int :
    dp = [[0] * (len(b) + 1) for _ in range(2)]
    
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + 1
            else:
                dp[i % 2][j] = max(dp[(i - 1) % 2][j], dp[i % 2][j - 1])
    
    return dp[len(a) % 2][len(b)]
    

s1 = input().strip()
s2 = input().strip()

print(lcs(s1, s2))