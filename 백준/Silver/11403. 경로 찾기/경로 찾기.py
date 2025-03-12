from collections import deque
import sys, heapq
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for i in range(n)]
visited = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph[j][i] and graph[i][k]:
                graph[j][k] = 1

for i in graph:
    print(*i)