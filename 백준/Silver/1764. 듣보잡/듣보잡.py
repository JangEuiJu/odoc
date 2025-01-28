import sys
input = sys.stdin.readline

N, M = map(int, input().split())
heard = {input().strip() for _ in range(N)}
seen = {input().strip() for _ in range(M)}

result = sorted(heard & seen)
    
print(len(result))
print('\n'.join(result))