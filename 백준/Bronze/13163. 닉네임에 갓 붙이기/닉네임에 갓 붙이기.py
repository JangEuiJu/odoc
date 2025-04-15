n = int(input())
for _ in range(n):
    nick = input().split()
    res = "god"

    for i in range(1, len(nick)):
        res += nick[i]

    print(res)
