import sys

def input():
    return sys.stdin.readline()

A = input().rstrip()
B = input().rstrip()
C = input().rstrip()
print(int(A) + int(B) - int(C))
print(int(A+B) - int(C))