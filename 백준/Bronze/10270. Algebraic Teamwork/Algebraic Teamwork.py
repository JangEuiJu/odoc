from sys import stdin
from math import factorial

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    res = factorial(n)
    print((res-1) % (10**9 + 7))