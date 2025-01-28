import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    temp = input().split()
    if len(temp) == 1:
        if temp[0] == 'all':
            S = set([i for i in range(1, 21)])
        else :
            S = set()
    else:
        func, x = temp[0], int(temp[1])
        if func == "add":
            S.add(x)
        elif func == "remove":
            S.discard(x)
        elif func == "check":
            print(1 if x in S else 0)
        elif func == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)