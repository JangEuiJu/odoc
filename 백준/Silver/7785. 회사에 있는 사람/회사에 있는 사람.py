import sys

def input():
    return sys.stdin.readline()

n = int(input())

temp = dict()

for _ in range(n):
    name, attendance = input().split()
    if attendance == 'enter':
        temp[name] = attendance
    elif attendance == 'leave':
        del temp[name]
        
t = sorted(temp.keys(), reverse = True)

for key in t:
    print(key)