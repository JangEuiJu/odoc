import sys, math
input = sys.stdin.readline


N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

res = 0
for i in range(len(size)):
    if(size[i] % T == 0):
        res += int(size[i] / T)
    else:
        res += (int(size[i] / T) + 1)
        

res2 = [int(sum(size) / P), sum(size) % P]

print(res)
print(*res2)