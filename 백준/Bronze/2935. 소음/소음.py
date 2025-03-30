# 실행 단축키 shift + f11

import sys
input = sys.stdin.readline

a = int(input())
oper = input().strip()
b = int(input())

if oper == "+":
    print(a + b)
else:
    print(a*b)