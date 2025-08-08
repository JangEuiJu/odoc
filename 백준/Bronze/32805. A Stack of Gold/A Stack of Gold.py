w, n = map(int, input().split())
t_w = n * (n + 1) // 2 * 29260
dif = w - t_w
print(dif // 110)