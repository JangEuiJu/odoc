N, price = int(input()), int(input())

candidates = [0]
if N >= 5: candidates.append(500)
if N >= 10: candidates.append(price // 10)
if N >= 15: candidates.append(2000)
if N >= 20: candidates.append(price // 4)

print(max(0, price - max(candidates)))
