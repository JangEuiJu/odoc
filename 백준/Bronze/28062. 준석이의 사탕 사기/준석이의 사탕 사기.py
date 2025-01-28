import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
odd_candy = []
result = 0

for i in arr:
    if i % 2 == 1:
        odd_candy.append(i)
    else:
        result += i
        
if len(odd_candy) % 2 == 1:
    odd_candy.sort()
    del odd_candy[0]
    result += sum(odd_candy)
else:
    result += sum(odd_candy)

print(result)