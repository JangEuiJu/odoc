N = int(input())
arr = list(map(int, input().split()))
cnt = 1
max_l = 1
for i in range(1, N):
    if arr[i-1] >= arr[i]:
        cnt += 1
    else:
        cnt = 1
    if max_l < cnt:
        max_l = cnt

cnt = 1
for i in range(1, N):
    if arr[i-1] <= arr[i]:
        cnt += 1
    else:
        cnt = 1
    if max_l < cnt:
        max_l = cnt
print(max_l)