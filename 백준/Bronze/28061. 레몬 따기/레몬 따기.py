n = int(input())
li = list(map(int, input().split()))
lemon = [li[i] - (n-i) for i in range(n)]
print(max(lemon))