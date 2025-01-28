import sys
input = sys.stdin.readline


yt, yj = map(int, input().split())
ytRes = True
yjRes = True

while(True):
    yj = yj + yt
    if yj >= 5:
        yjRes = False
        break
    yt = yt + yj
    if yt >= 5:
        ytRes = False
        break
    
if ytRes == False:
    print("yj")
if yjRes == False:
    print("yt")