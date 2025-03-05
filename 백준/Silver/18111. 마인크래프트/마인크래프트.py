import sys, heapq
input = sys.stdin.readline

n, m, b = map(int, input().split())
res, level = int(1e9), 0
arr = []
for _ in range(n):
    arr.append([int(i) for i in input().rstrip().split()])

for i in range(257):
    use = 0
    take = 0
    for x in range(n):
        for y in range(m):
            if arr[x][y] > i:
                take += arr[x][y] - i
            else:
                use += i - arr[x][y]
    
    if use > take + b:
        continue
    
    cnt = take * 2 + use
    if cnt <= res:
        res = cnt
        level = i

print(res, level)