import sys
input = sys.stdin.readline

T = int(input())

def function(x):
    mylist = []
    for i in range(1,x+1):
        if x % i == 0:
            mylist.append(i)
    return mylist

for i in range(T):
    number = int(input())  
    listlist = function(number)  
    TF = True
    if sum(function(listlist[-1]))-listlist[-1] <= listlist[-1]:
        print('BOJ 2022')
        TF = False
    else:
        for j in range(len(listlist)-1):
            if sum(function(listlist[j]))-listlist[j] > listlist[j]:
                print('BOJ 2022')
                TF = False
                break
        if TF:
                print('Good Bye')