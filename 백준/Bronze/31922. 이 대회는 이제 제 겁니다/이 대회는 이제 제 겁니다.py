import sys
input = sys.stdin.readline

A, P, C = map(int, input().split())

print(max(A + C, P))