import sys
input = sys.stdin.readline


T = int(input())

for _ in range (T):
    k = int(input())
    n = int(input())
    arr = [x for x in range(1, n + 1)]
    for i in range(k):
        for j in range(1, n):
            arr[j] += arr[j-1]
    print(arr[-1])