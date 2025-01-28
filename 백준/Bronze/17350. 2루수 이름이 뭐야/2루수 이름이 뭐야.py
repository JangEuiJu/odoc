import sys
input = sys.stdin.readline

N = int(input())
name = []

for i in range(N):
    name.append(input().strip())

if "anj" in name:
    print("뭐야;")
else:
    print("뭐야?")