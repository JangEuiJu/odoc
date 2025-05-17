import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort() 

visited = [False] * n
result = []

def backtracking():
    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            result.append(nums[i])
            backtracking()
            result.pop()
            visited[i] = False

backtracking()