a, b, c = map(int, input().split())

def power(a, b):
    result = 1
    
    while b:
        if b % 2 == 1:
            result *= a
        a *= a
        a = a % c
        b = b // 2
        
    return result

print(power(a,b) % c)