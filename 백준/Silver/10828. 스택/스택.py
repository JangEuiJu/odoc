import sys

input = sys.stdin.readline

stack = []

N = int(input().strip())

for _ in range (N) :
    command = input().strip().split()
    if command[0] == 'push':
        stack.append(int(command[1]))
    elif command[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(0 if stack else 1)
    elif command[0] == 'top':
        print(stack[-1] if stack else -1)