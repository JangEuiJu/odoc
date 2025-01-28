import sys
input = sys.stdin.readline 


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
cntW, cntB = 0, 0

def daq(r, c, n):
    global cntW, cntB
    color = arr[r][c]
    for i in range(r, r+n):
        for j in range(c, c+n):
            if color != arr[i][j]:
                daq(r, c, n // 2)
                daq(r, c + n//2, n // 2)
                daq(r + n//2, c, n // 2)
                daq(r + n//2, c + n//2, n // 2)
                return
    if color == 0:
        cntW += 1
    else:
        cntB +=1


daq(0, 0, n)
print(cntW)
print(cntB)