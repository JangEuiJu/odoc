import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    if arr[i] < 250:
        arr[i] = 4
    elif arr[i] < 275:
        arr[i] = 3
    elif arr[i] < 300:
        arr[i] = 2
    else:
        arr[i] = 1
        
for value in arr:
    print(value, end=" ")