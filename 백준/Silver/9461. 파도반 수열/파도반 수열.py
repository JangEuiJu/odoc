import sys

input = sys.stdin.readline 
t = int(input())
dp = [0] * 100
for i in range(t):
    n = int(input())
    if n == 1 or n == 2:
        print(1)
    else:
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-3]
        print(dp[n])