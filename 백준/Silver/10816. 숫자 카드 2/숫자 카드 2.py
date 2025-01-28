import sys
input = sys.stdin.readline

from collections import Counter

N = int(input())
arr = list(map(int, input().split()))

M = int(input())
arr2 = list(map(int, input().split()))

count = Counter(arr)
answer = []

for i in range(M):
    answer.append(count.get(arr2[i], 0))
    
print(*answer)