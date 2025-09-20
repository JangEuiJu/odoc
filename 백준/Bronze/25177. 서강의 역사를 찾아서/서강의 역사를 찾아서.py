N, M = map(int, input().split())
a = list(map(int, input().split()))	
b = list(map(int, input().split()))	
 
if N < M :
    a += [0] * (M-N)
 
result = 0
for i in range(M) :
    result = max(result, b[i] - a[i])
 
print(result)