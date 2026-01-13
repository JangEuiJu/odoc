from collections import deque

def bfs(node):
    q = deque()
    q.append(node)
    check[node] = 0
    while q:
        node = q.popleft()
        for n in graph[node]:
            if check[n] == -1:
                q.append(n)
                check[n] = check[node]+1

for _ in range(int(input())):
    a = input().split()
    N, M = int(a[0]), int(a[1])
    vx = a[-1]
    graph = [[] for i in range(N+1)]
    li = a[2:-1]
    for i in range(M):
        u, v = int(li[i*2][1:]), int(li[i*2+1][1:])
        graph[u].append(v)
        graph[v].append(u)
    check = [-1]*(N+1)
    bfs(int(vx[1:]))
    res = sum([1 for t in check if 1 <= t <= 2])
    print(f"The number of supervillains in 2-hop neighborhood of {vx} is {res}")