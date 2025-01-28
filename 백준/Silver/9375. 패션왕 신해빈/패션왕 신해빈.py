
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    cloth = {}
    for i in range(n):
        name, categori = input().strip().split()
        if categori in cloth:
            cloth[categori].append(name)
        else:
            cloth[categori] = [name]
    
    cnt = 1
    for k in cloth:
        cnt *= (len(cloth[k]) + 1)
        
    print(cnt - 1)