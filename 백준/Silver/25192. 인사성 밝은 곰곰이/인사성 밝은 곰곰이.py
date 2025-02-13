arr = set()
cnt = 0
n = int(input())

for i in range(n):
    str = input()
    if str != "ENTER":
        if str not in arr:
            cnt += 1
            arr.add(str)
    elif str == "ENTER" : 
        arr.clear()

print(cnt)