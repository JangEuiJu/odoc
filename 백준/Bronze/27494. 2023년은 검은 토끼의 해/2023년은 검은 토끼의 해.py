import sys
input = sys.stdin.readline

n = int(input())
if n < 2023: 
    print(0)
else:
    ans = 0
    for i in range(2023, n + 1):
        x = str(i)
        if not {'2', '3', '0'}.issubset(set(x)): 
            continue
        tmp = []
        for j in x: 
            if j == '2' and len(tmp) in [0, 2]:
                tmp.append(j)
            elif j == '0' and len(tmp) == 1:
                tmp.append(j)
            elif j =='3' and len(tmp) == 3:
                ans += 1 
                break
    print(ans)