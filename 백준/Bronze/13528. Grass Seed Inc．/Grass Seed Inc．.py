import sys
input = sys.stdin.readline

n = float(input())
l = int(input())

res = 0.0
for _ in range(l):
    x, y = map(float, input().split())
    temp = x * y
    res += temp
    
    
print(res * n)