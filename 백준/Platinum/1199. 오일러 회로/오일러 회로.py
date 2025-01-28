import sys
input = sys.stdin.readline

path = []
def euler(graph, now, n):
    stack = []
    stack.append(now)
    path = []
    while stack:
        now = stack[-1]
        if graph[now]:
            for near, cnt in graph[now].items():
                graph[now][near] -= 1
                graph[near][now] -= 1
                if graph[now][near] == 0:
                    graph[now].pop(near)
                    graph[near].pop(now)
                stack.append(near)
                break
        else:
            path.append(now+1)
            stack.pop()
    return path
        
def main():
    n = int(input())
    adj = [list(map(int, input().split())) for _ in range(n)]
    graph = [dict() for _ in range(n)]
    for i in range(n):
        degree = 0
        for j in range(n):
            degree += adj[i][j]
            if adj[i][j]:
                graph[i][j] = adj[i][j]
        if degree % 2 :
            print(-1)
            return
    print(*euler(graph, 0, n))

main()