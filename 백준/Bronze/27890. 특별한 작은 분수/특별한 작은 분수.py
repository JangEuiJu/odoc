import sys

X, N=map(int,sys.stdin.readline().split())

for i in range(N):

    if X%2==0:
        X=int(X/2)^6
    else:
        X=int(2*X)^6

print(X)