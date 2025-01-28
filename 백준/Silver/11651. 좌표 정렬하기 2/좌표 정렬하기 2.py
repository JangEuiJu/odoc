import sys
input = sys.stdin.readline


N = int(input())

coord = []
for _ in range(N) :
    a, b = map(int, input().split())
    coord.append((a, b))
    
coord.sort(key = lambda x: (x[1], x[0]))

for x, y in coord:
    print(x, y)