import sys
input = sys.stdin.readline

def dolmen(a: int, b: int) -> int:
    return (a + b) * (a + b - 1) * (a + b) // 2

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(dolmen(a, b))

