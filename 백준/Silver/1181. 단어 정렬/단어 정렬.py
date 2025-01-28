import sys
input = sys.stdin.readline


N = int(input())

arr = []

for _ in range(N):
    arr.append(input().rstrip())
    
result_arr = sorted(set(arr), key = lambda criteria : (len(criteria), criteria))

print("\n".join(result_arr))