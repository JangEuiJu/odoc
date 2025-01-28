import math
import sys

def input():
    return sys.stdin.readline()

a, b = map(int, input().split())
print(math.gcd(a, b))
print(math.lcm(a, b))