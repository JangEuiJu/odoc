import sys
input = sys.stdin.readline


N = int(input())
people = []
people_rank = []

for _ in range(N):
    weight, height = map(int, input().split())
    people.append((weight, height))
    

for i in range(N):
    rank = 1
    for j in range(N):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1
    people_rank.append(rank)


for rank in people_rank:
   print(rank, end = " ") 