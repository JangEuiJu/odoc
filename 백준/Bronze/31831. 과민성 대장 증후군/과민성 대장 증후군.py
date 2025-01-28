import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

result = []
stress = 0
for i in range(N):
    stress = stress + arr[i]
    if stress <= 0 :
        stress = 0
    result.append(stress)

count = 0
for i in range(N):
    if result[i] >= M:
        count = count + 1
        
print(count)