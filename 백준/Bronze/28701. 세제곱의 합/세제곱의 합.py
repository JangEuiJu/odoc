import sys
input = sys.stdin.readline

n = int(input())

s = 0
t = 0

for i in range(1, n+1):
    s += i
    t += i**3

print(s)
print(s**2)
print(t)