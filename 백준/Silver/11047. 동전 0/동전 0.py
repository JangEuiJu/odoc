import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = []
count = 0

for _ in range(N):
    A.append(int(input()))


def find_max(arr, criteria):
    filtered = [x for x in arr if x <= criteria]
    if filtered:
        return max(filtered)
    else:
        return None

while K:
    val = find_max(A, K)
    plus_val = K // val
    count = count + plus_val
    K = K - val*plus_val

print(count)