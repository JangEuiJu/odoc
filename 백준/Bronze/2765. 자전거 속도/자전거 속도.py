from math import pi
import sys
input = sys.stdin.readline

i = 1
while True:
    d, r, t = map(float, input().split())
    if r == 0:
        break
    dis = d/63360 * pi * r
    mph = dis / t * 3600
    print("Trip #%d: %.2f %.2f" % (i, dis, mph))
    i += 1