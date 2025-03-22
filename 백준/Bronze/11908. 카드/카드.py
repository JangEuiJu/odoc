import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
arr = sorted(list(map(int, input().split())))
print(sum(arr[:-1]))
