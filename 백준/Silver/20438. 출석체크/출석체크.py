import sys
input = sys.stdin.readline

n, k, q, m = map(int, input().split())

sleep = [False for _ in range(n+3)]
for i in map(int, input().split()):
    sleep[i] = True

check = [1 for _ in range(n+3)]

for i in map(int, input().split()):
    if sleep[i]:
        continue

    for j in range(i, n+3, i):
        if sleep[j]:
            continue

        check[j] = 0

sum_ = 0
check[2] = 0
for i in range(3, n+3):
    if check[i]:
        sum_ += 1

    check[i] = sum_

for _ in range(m):
    s, e = map(int, input().split())
    print(check[e] - check[s-1])