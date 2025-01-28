import sys

n = int(sys.stdin.readline())

arr = [0] * 21
arr[0] = 0
arr[1] = 1

for i in range (2,21) :
  arr[i] = arr[i-1] + arr[i-2]

print(arr[n])