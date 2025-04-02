# 실행 단축키 shift + f11

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v = int(input().strip())
tree = {}

for _ in range(v-1):
    a, b, c = map(int, input().split())
    if a not in tree:
        tree[a] = []
    if b not in tree:
        tree[b] = []
    tree[a].append((b, c))
    tree[b].append((a, c))

def dfs(node, dist):
    global max_dist, farthest_node
    visited[node] = True

    if dist > max_dist:
        max_dist = dist
        farthest_node = node

    for child, weight in tree.get(node, []):  # 존재하지 않는 키 방지
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
