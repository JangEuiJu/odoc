total = 0
for i in range(5):
    point = int(input())
    if point < 40:
        point = 40
    total += point
average = int(total / 5)
print(average)