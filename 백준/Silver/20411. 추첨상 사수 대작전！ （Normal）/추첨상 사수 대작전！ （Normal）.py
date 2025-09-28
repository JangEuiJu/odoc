
m, seed, x1, x2 = map(int, input().split())
ans, sq = 1, seed-x1
for i in reversed(bin(m-2)[2:]):
    if i == '1':
        ans = (ans*sq)%m
    sq = (sq*sq)%m
a = (ans*(x1-x2))%m
c = (x1-(a*seed))%m
print(a, c)