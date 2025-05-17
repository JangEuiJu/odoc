# #실행 단축키 shift + f11

from itertools import permutations
import sys
input = sys.stdin.readline 

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

perm_set = set(permutations(numbers, M))
perm_list = sorted(list(perm_set))

for p in perm_list:
    print(' '.join(map(str, p)))
