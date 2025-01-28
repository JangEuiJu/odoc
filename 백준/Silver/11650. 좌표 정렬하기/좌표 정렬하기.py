import sys
input = sys.stdin.readline


N = int(input())

coord = []
for _ in range(N) :
    a, b = map(int, input().split())
    coord.append((a, b))
    
coord.sort()

for x, y in coord:
    print(x, y)