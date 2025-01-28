import sys

input = sys.stdin.readline
N, M = map(int, input().split())
S = []

for i in range(N):
    S.append(input())

answer = 0

for _ in range(M):
    t = input()
    if t in S:
        answer += 1

print(answer)    
