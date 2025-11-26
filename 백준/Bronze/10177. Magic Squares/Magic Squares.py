import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)] 
    target = sum(arr[0]) 
    col = 0
    leftDiagonal = 0 
    rightDiagonal = 0 
    isMagic = True 

    for i in range(n):
        if target != sum(arr[i]):
            isMagic = False
            break   
        leftDiagonal += arr[i][i]
        rightDiagonal += arr[i][-(i+1)]
        
        if i == n - 1:
            if leftDiagonal != target:
                isMagic = False
                break
            elif rightDiagonal != target:
                isMagic = False
                break
        for j in range(n):
            col += arr[j][i]
            if j == n - 1:
                if col != target:
                    isMagic = False
                    break
                col = 0
    
    print("Magic square of size %d"%n if isMagic == True else "Not a magic square")