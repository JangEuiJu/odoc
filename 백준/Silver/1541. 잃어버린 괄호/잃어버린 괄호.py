import sys
input = sys.stdin.readline 

expression = input().strip()
number = []
oper = []
temp = ""

for char in expression:
    if char in "+-":
        number.append(int(temp))
        oper.append(char)
        temp = ""
    else:
        temp += char

number.append(int(temp))
    

result = number[0]
check = False

for i in range(len(oper)):
    if oper[i] == "-":
        check = True
        
    if check:
        result -= number[i + 1]
    else:
        result += number[i + 1]

print(result)