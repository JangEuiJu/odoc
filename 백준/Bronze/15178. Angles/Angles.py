import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())
    print(a, b, c)
    if a+b+c == 180:
        print("Seems OK")
    else:
        print("Check")