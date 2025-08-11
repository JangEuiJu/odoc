n = int(input())
eggplant = list(input().split())
m, k = map(int, input().split())
 
result = False
 
for i in range(m):
    plants = list(map(int, input().split()))
    isW = True
    for k in plants:
        if eggplant[k-1] == 'P':
            isW = False
            break
    if isW:
        result = True
 
if result:
    print('W')
else:
    print('P')