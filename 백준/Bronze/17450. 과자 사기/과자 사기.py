res, ans = 0, 0
snack = ["S", "N", "U"]
for i in range(3):
    cost, weight = map(int, input().split())
    tcost, tweight = cost * 10, weight * 10
    money = tcost - 500 if tcost >= 5000 else tcost
    if (tweight / money) > res:
        res = tweight / money
        ans = i
print(snack[ans])