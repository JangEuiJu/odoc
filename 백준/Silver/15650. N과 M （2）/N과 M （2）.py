# 실행 단축키 shift + f11

import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())

for comb in combinations(range(1, n + 1), m):
    print(' '.join(map(str, comb)))
