import sys

T = int(sys.stdin.readline())

for t in range(1, T + 1):
    I = sys.stdin.readline().rstrip()
    P = sys.stdin.readline().rstrip()

    i = 0
    d = 0

    for p in P:
                
        if len(I) <= i or p != I[i]:
            d += 1
            continue
        
        i += 1

    if len(I) == i:
        print(f'Case #{t}: {d}')
    else:
        print(f'Case #{t}: IMPOSSIBLE')