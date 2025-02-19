
import sys, heapq

input = sys.stdin.readline 

n = int(input())
arr = list(map(int, input().split()))

res = 0
left, distinct = 0, 0
count = {}

for right in range(n):
    if arr[right] in count:
        count[arr[right]] += 1
    else :
        count[arr[right]] = 1
        distinct += 1
    
    while distinct > 2 :
        count[arr[left]] -= 1
        if count[arr[left]] == 0:
            del count[arr[left]]
            distinct -= 1
        left += 1
        
    res = max(res, right-left+1)

print(res)
    