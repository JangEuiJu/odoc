# 실행 단축키 shift + f11

import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    
def dijkstra(start):
    distances = [float("inf")] * (V + 1)
    distances[start] = 0
    q = []
    heapq.heappush(q, (distances[start], start))
    
    while q:
        cnt_distance, node = heapq.heappop(q)
        if distances[node] < cnt_distance:
            continue
        
        for adj_node, distance in graph[node]:
            cal_distance = distances[node] + distance
            if cal_distance < distances[adj_node]:
                distances[adj_node] = cal_distance
                heapq.heappush(q, (cal_distance, adj_node))
                
    return distances

result = dijkstra(start)

for i in range(1, len(result)):
    print("INF" if result[i] == float('inf') else result[i])