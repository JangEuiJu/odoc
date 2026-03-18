a2, a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if c == a2:
    result = (a1 <= 0 and ((c - a2) * n0 * n0 - (a1 * n0) - a0) >= 0)
elif a2 > c:  
    result = False
else:  
    if a1 > 2 * (c - a2) * n0: 
        result = (a1 * a1 + 4 * a0 * (c - a2) <= 0)
    else:  
        result = ((c - a2) * n0 * n0 - (a1 * n0) - a0 >= 0)

print(1 if result else 0)