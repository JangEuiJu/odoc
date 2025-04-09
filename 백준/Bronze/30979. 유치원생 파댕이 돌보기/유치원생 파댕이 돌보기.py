t = int(input())
n = int(input())
f = list(map(int, input().split()))

if t <= sum(f):
    print("Padaeng_i Happy")
else:
    print("Padaeng_i Cry")