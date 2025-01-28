import sys, math
input = sys.stdin.readline

def isPrime(num):
    if num < 2:
        return False
    for i in range (2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    
    return True

M, N = map(int, input().split())

arr = []

for i in range(M, N+1):
    if isPrime(i):
        print(i)
