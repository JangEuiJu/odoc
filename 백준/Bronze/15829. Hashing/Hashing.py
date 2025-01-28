import sys
input = sys.stdin.readline


L = int(input())
M = 1234567891
r = 31
inputString = input()


answer = 0
for i in range(L):
    num = ord(inputString[i]) - 96
    sigma = num * (r ** i)
    answer += sigma

print(answer % M)