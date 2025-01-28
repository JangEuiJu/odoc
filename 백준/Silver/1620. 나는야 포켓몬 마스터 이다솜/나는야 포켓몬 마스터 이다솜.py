import sys

def input():
    return sys.stdin.readline()

N, M = map(int, input().split())

arr = {}
reverse_arr = []

for i in range(N):
    name = input().rstrip()
    arr[name] = i+1
    reverse_arr.append(name)
    
for _ in range(M):
    query = input().rstrip()
    if query.isdigit():
        print(reverse_arr[int(query)-1])
    else:
        print(arr[query])

