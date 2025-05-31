a, b, x, y = map(int, input().split())
a, b = min(a, b), max(a, b)
x, y = min(x, y), max(x, y) 
d = b-a 
t = abs(x-a)+abs(y-b)
ans = min(d, t)
    
print(ans)