t = int(input())

for _ in range(t):
    a_len, b_len = map(int, input().split())
    a = set(list(map(int, input().split())))
    b = set(list(map(int, input().split())))
    
    if a == b: 
        print("=")
    elif a < b:
        print("<")
    elif b < a:
        print(">")
    else:
        print("?")