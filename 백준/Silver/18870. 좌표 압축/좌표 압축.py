import sys
input = sys.stdin.readline

n = int(input())
coord = list(map(int, input().split()))
sort = sorted(list(set(coord)))

dic = {sort[i] : i for i in range(len(sort))}

for i in coord:
    print(dic[i], end = " ")