import sys

K = int(sys.stdin.readline())

for k in range(1, K + 1):
    N, M = map(int, sys.stdin.readline().split())

    property_price = dict()

    for _ in range(N):
        S, C = sys.stdin.readline().rstrip().split()
        C = int(C)

        property_price[S] = C
    
    P = sys.stdin.readline().rstrip().split()

    min_price = 0
    max_price = 0
    unknown_count = 0

    for p in P:
        
        if p == '?':
            unknown_count += 1
            continue
        
        min_price += property_price[p]
        max_price += property_price[p]

        del property_price[p]
    
    if unknown_count != 0:
        sorted_price = sorted(property_price.values())

        min_price += sum(sorted_price[:unknown_count])
        max_price += sum(sorted_price[-unknown_count:])
    
    print(f'Data Set {k}:')
    print(f'{min_price} {max_price}')
    print()