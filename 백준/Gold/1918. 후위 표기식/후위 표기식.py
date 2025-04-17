# 실행 단축키 shift + f11

import sys
from itertools import combinations
input = sys.stdin.readline

expression = input()
length = len(expression)
stack = []

for i in range(length):
    s = expression[i]
    if s.isalpha():
        print(s, end = "")
    elif s == "(":
        stack.append(s)
    elif s == "*" or s == "/":
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            print(stack.pop(), end = "")
        stack.append(s)
    elif s == "+" or s =="-":
        while stack and stack[-1] != "(":
            print(stack.pop(), end = "")
        stack.append(s)
    elif s == ")":
        while stack and stack[-1] != "(":
            print(stack.pop(), end = "")
        stack.pop()

while stack:
    print(stack.pop(), end="")