import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
li = []
for i in range(N):
    score = float(input())
    li.append(score)

li.sort()
js = sum(li[K:N-K]) / (N - K * 2)
bs = (sum(li[K:N-K]) + li[K] * K + li[N-K-1] * K) / N
print("%.2f" % (js + 1e-8))
print("%.2f" % (bs + 1e-8))