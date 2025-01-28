import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

result = 0
temp = 0

for i in range(n):
    temp = temp + arr[i]
    result += temp
    
print(result)