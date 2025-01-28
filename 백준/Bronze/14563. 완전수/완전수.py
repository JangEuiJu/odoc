import sys
input = sys.stdin.readline

def judge(num):
    arr = []
    for i in range(1, num):
        if num % i == 0:
            arr.append(i)
    return arr
            
    

t = int(input())
number = list(map(int, input().split()))


for i in number:
    arr = judge(i)
    if sum(arr) > i:
        print("Abundant")
    elif sum(arr) < i:
        print("Deficient")
    else:
        print("Perfect")