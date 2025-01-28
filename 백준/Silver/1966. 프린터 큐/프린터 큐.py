import sys, math
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    
    result = 1
    while data :
        if data[0] < max(data):
            data.append(data.pop(0))
        else :
            if M == 0 : break
            
            data.pop(0)
            result += 1
            
        M = M - 1 if M > 0 else len(data) - 1
        
    print(result)