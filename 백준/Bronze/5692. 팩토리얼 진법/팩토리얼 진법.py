import sys

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

while True:
    num = sys.stdin.readline().strip()
    if int(num) == 0:
        break    
    n = len(num)
    print(sum(map(lambda x : int(num[x])*factorial(n-x), range(n))))