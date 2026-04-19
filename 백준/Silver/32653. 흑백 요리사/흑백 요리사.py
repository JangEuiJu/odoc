import sys
input = sys.stdin.readline
from math import lcm

N = int(input())
A = list(map(lambda x: 2*int(x), input().split()))
print(lcm(*A))