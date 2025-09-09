n, m = map(int, input().split())
graph = [[-1] * (m + 1) for _ in range(n + 1)]
col = list(map(int, input().split()))
row = list(map(int, input().split()))

for i in range(1, n + 1):
    graph[i][0] = col[i - 1]
for j in range(1, m + 1):
    graph[0][j] = row[j - 1]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        graph[i][j] = graph[i][j - 1] ^ graph[i - 1][j]

print(graph[n][m])