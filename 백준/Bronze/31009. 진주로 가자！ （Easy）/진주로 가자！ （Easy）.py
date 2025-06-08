n = int(input())
b = []
res1 = res2 = 0

for _ in range(n):
    d, c = input().split()
    b.append([d, int(c)])
    if d == "jinju":
        res1 = int(c)

for i in b:
    if i[1] > res1:
        res2 += 1

print(res1)
print(res2)