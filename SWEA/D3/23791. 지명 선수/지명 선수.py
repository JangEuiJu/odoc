t = int(input())

for _ in range(t):
    n = int(input())
    a_prefer = list(map(int, input().split()))
    b_prefer = list(map(int, input().split()))
    
    available = list(range(1, n+1))
    
    team = [''] * n
    
    turn_a = True
    while available:
        if turn_a:
            for p in a_prefer:
                if p in available:
                    team[p-1] = 'A'
                    available.remove(p)
                    break
        else:
            for p in b_prefer:
                if p in available:
                    team[p-1] = 'B'
                    available.remove(p)
                    break
        turn_a = not turn_a
    
    print(''.join(team))     