import sys
input = sys.stdin.readline

n = int(input())
f = int(input())
ans = f
for _ in range(n):
    i, j = map(int, input().split())
    f += (i-j)
    if f < 0: ans = 0;break
    ans = max(ans, f)
print(ans)