import sys, heapq
input = sys.stdin.readline 


n = int(input())
m = int(input())
s = input().strip()

cnt, i, pattern_count = 0, 0, 0

while i < m - 1:
    if s[i:i+3] == "IOI":  
        pattern_count += 1
        if pattern_count >= n:
            cnt += 1  
        i += 2  
    else:
        pattern_count = 0  
        i += 1  

print(cnt)

    