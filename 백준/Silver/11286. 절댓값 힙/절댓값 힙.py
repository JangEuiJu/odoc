import sys, heapq

input = sys.stdin.readline 

n = int(input())
abs_heap = []
for i in range (n):
    num = int(input())
    if num != 0:
        heapq.heappush(abs_heap, (abs(num), num))
    else :
        if abs_heap:
            print(heapq.heappop(abs_heap)[1])
        else:
            print(0)