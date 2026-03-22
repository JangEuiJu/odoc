a, b = map(int, input().split())

sq = []

for i in range(1, b+1):
  for j in range(i):
    sq.append(i)

result = sum(sq[a-1:b])

print(result)