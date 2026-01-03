import sys

input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()
answer = 4 

for i in range(N):
    start = i
    end = N-1
    while start < end:
        if nums[end]-nums[start] > 4:
            end -=1
        else:
            temp_answer = 4 - (end-start)
            answer = min(answer,temp_answer)
            break
print(answer)