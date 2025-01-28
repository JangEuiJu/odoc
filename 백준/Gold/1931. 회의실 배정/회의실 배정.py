import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort(key=lambda x : (x[1], x[0]))

cnt = 0
end = 0
for x, y in arr:
    if end <= x:
        end = y
        cnt += 1
        
print(cnt)