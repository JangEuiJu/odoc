import sys, math
input = sys.stdin.readline


N = int(input())

factorial_num = str(math.factorial(N))

res = 0
for i in range(len(factorial_num) -1, -1, -1):
    if(factorial_num[i] == '0'):
        res += 1
    else:
        break
print(res)