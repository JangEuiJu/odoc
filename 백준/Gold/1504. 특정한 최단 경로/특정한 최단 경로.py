# 실행 단축키 shift + f11

import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

n, e = map(int, input().split())
graph = [[] for _ in range (n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
def dijkstra(start):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
    return distance
    
    
v1, v2 = map(int, input().split())

start_first_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

result = min((start_first_distance[v1] + v1_distance[v2] + v2_distance[n]),
             (start_first_distance[v2] + v2_distance[v1] + v1_distance[n]))

print(result if result < INF else -1)