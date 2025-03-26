# 실행 단축키 shift + f11

import sys
from collections import deque
input = sys.stdin.readline

def edit_distance (s1, s2):
    l1, l2 = len(s1), len(s2)
    
    dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
    
    for i in range(l1 + 1):
        dp[i][0] = i
    for j in range(l2 + 1):
        dp[0][j] = j
    
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else :
                dp[i][j] = min(
                    dp[i - 1][j] + 1,
                    dp[i][j - 1] + 1,
                    dp[i - 1][j - 1] + 1,
                )

    return dp[l1][l2]
    
    
s1 = input().rstrip()
s2 = input().rstrip()
print(edit_distance(s1, s2))