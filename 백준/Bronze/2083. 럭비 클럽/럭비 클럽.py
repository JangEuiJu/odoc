import sys
input = sys.stdin.readline

while(True):
    a, b, c = map(str, input().split())
    if a == '#' and b == '0' and c == '0': break
    if int(b) > 17 or int(c) >= 80:
        print(a, "Senior")
    else:
        print(a, "Junior")