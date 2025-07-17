n = int(input())
line = input()
half = n / 2
cnt = line.count('O')
print("Yes" if cnt >= half else "No")