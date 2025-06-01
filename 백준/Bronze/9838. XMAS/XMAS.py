n = int(input())
lst = [0] * (n + 1)
for i in range(1, n + 1) :
    lst[int(input())] = i
for i in range(1, n + 1) : print(lst[i])