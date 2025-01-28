import sys
input = sys.stdin.readline


N, K = map(int, input().split())

people = list(range(1, N+1))
index = 0
result = []

while(len(people) > 0):
    index = (index + K - 1) % len(people)
    result.append(people.pop(index))
    

print("<", ", ".join(map(str, result)), ">", sep="")