n, m, a, b = map(int, input().split())
res = (n * 3 - m) * a + b if n * 3 - m > 0 else 0
print(res)