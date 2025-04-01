# 실행 단축키 shift + f11

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v = int(input())
tree = {i : [] for i in range(1, v + 1)}

for _ in range(v):
    info = list(map(int, input().split()))
    node = info[0]
    index = 1
    while info[index] != -1:
        child = info[index]
        distance = info[index + 1]
        tree[node].append((child, distance))
        index += 2
        
def dfs(node, dist):
    global max_dist, farthest_node
    visited[node] = True
    
    if dist > max_dist:
        max_dist = dist
        farthest_node = node
        
    for child, weight in tree[node]:
        if not visited[child]:
            dfs(child, dist + weight)


visited = [False] * (v + 1)
max_dist = 0
farthest_node = 0
dfs(1, 0)

visited = [False] * (v + 1)
max_dist = 0
dfs(farthest_node, 0)

print(max_dist)