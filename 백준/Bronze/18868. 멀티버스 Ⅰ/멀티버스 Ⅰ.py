m, n = map(int, input().split())
universe = [list(map(int, input().split())) for _ in range(m)]
cnt = 0

for planet in range(m):
    for i in range(m):
        arr_sort = sorted(universe[i]) 
        idx = []
        for j in universe[i]:  
            idx.append(arr_sort.index(j) + 1)
        universe[i] = idx

for i in range(m - 1):
    for j in range(i + 1, m):
        if universe[i] == universe[j]: 
            cnt += 1

print(cnt)