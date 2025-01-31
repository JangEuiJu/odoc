import sys
import heapq

input = sys.stdin.readline 


T = int(input())

for _ in range(T):
    K = int(input())
    min_heap = []
    max_heap = []
    exists = {}
    
    for i in range(K):
        instr = input().split()
        if instr[0] == "I":
            heapq.heappush(min_heap, int(instr[1]))
            heapq.heappush(max_heap, -int(instr[1]))
            exists[int(instr[1])] = exists.get(int(instr[1]), 0) + 1
        else:
            if len(exists) == 0:
                continue
            
            if instr[1] == "1":
                while max_heap:
                    max_val = -heapq.heappop(max_heap)
                    if exists.get(max_val, 0) > 0:
                        exists[max_val] -= 1
                        if exists[max_val] == 0:
                            del exists[max_val]
                        break         
            else:
                while min_heap:
                    min_val = heapq.heappop(min_heap)
                    if exists.get(min_val, 0) > 0:
                        exists[min_val] -= 1
                        if exists[min_val] == 0:
                            del exists[min_val]
                        break
    
    if len(exists) == 0:
        print("EMPTY")
    else:
        while max_heap:
            max_val = -heapq.heappop(max_heap)
            if exists.get(max_val, 0) > 0:
                break  

        while min_heap:
            min_val = heapq.heappop(min_heap)
            if exists.get(min_val, 0) > 0:
                break  

        print(max_val, min_val) 