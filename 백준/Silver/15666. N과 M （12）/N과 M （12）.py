N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

result = []

def backtrack(start, path):
    if len(path) == M:
        result.append(tuple(path))
        return
    for i in range(start, N):
        backtrack(i, path + [nums[i]]) 
        
backtrack(0, [])

result = sorted(set(result))

for seq in result:
    print(' '.join(map(str, seq)))
