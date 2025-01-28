import sys
input = sys.stdin.readline


str = input()
temp = []

for i in str:
    if i.isdigit():
        temp.append(int(i))
        


if (temp[0] + temp[1]) == temp[2]:
    print("YES")
else : 
    print("NO")