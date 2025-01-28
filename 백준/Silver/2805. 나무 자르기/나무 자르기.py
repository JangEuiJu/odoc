import sys
input = sys.stdin.readline 


N, M = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, max(arr)
result = 0

while start <= end:
    mid = (start + end) // 2
    checknum = 0
    
    checknum = sum(height - mid for height in arr if height > mid)
    
    if checknum >= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)