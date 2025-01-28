import sys
input = sys.stdin.readline


N = int(input())
arr = set(map(int, input().split()))


M = int(input())
check = list(map(int, input().split()))
for i in range(M):
    if check[i] in arr:
        print(1)
    else:
        print(0)