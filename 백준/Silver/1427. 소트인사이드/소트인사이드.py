import sys

def input():
    return sys.stdin.readline()

N = input()

M = sorted(N, reverse = True)

for i in M: 
    print(i, end="")