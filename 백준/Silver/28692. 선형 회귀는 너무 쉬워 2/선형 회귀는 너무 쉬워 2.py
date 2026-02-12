import sys
input = sys.stdin.readline

N = int(input())
S_x, S_y, S_xy, S_xx = 0, 0, 0, 0
for _ in range(N):
    x_i, y_i = map(int, input().rstrip().split())
    S_x += x_i
    S_y += y_i
    S_xy += x_i*y_i
    S_xx += x_i*x_i
if S_x*S_x != N*S_xx:
    a_2 = (N*S_xy - S_x*S_y)/(N*S_xx - S_x*S_x)
    b_2 = (S_y - a_2*S_x)/N
    print(a_2, b_2)
else:
    print("EZPZ")