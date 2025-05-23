n = int(input())
lst = [input() for _ in range(0, n)]

for i in range(0, len(lst)):
    str = lst[i]
    print(str[::-1])