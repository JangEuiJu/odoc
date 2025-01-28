import sys
from copy import deepcopy
input = sys.stdin.readline


scan = input().strip()
N = []
for _ in range(int(input())):
    N.append(input().strip())
N1 = deepcopy(N)
for i in N: 
    for j in range(len(i)):
        if scan[j] != '*':
            if scan[j] != i[j]:
                N1.pop(N1.index(i))
                break

print(len(N1))
for i in N1:
    print(i)