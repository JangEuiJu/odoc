### 실행 단축키 shift + f11
import sys
input = sys.stdin.readline

k = int(input())

for i in range(k):
    arr = list(map(int, input().split()))
    del arr[0]
    arr.sort()
    gap = []
    
    print("Class", (i+1))
    
    for j in range(len(arr) - 1):
        gap.append(arr[j+1] - arr[j])
    
    print("Max", str(max(arr)) + "," , "Min", str(min(arr)) + ",", "Largest gap", max(gap))