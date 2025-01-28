import sys
input = sys.stdin.readline


for _ in range(3):
    n = int(input())
    arr = [int(input()) for i in range(n)]
    if sum(arr) == 0:
        print(0)
    elif sum(arr) < 0:
        print('-')
    else:
        print('+')