import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
arr = [0] * N

for i in range(N):
    arr[i] = int(input())

arr.sort()

print(round(sum(arr) / N))
print(int(arr[N // 2]))

counter = Counter(arr)
modes = counter.most_common()
max_count = modes[0][1]
candidates = [num for num, count in modes if count == max_count]
if len(candidates) > 1 :
    candidates.sort()
    print(candidates[1])
else:
    print(candidates[0])

print(max(arr) - min(arr))