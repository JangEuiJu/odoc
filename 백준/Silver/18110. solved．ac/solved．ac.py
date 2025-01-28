import sys
input = sys.stdin.readline

def my_round(val):
    if val - int(val) >= 0.5:
        return int(val)+1
    else:
        return int(val)

N = int(input())

if N == 0:
    print(0)
else :
    arr = [int(input()) for _ in range(N)]

    arr.sort()
    rmv = my_round(N * 0.15)

    arr = arr[rmv:N-rmv]
    
    print(my_round(sum(arr) / len(arr)))