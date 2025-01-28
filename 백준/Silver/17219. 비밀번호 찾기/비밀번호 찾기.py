import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}

for _ in range(n):
    site, pw = input().strip().split()
    dict[site] = pw

for _ in range(m):
    find = input().strip()
    print(dict[find])