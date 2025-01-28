import sys, math
input = sys.stdin.readline


N, K= map(int, input().split())

print(math.factorial(N) // (math.factorial(N-K)*math.factorial(K)))
