import sys

while True:
    a, b = sys.stdin.readline().rstrip().split()

    if a == '0' and b == '0':
        break
    
    if len(a) < len(b):
        a = a.zfill(len(b))
    elif len(b) < len(a):
        b = b.zfill(len(a))
    
    count = 0

    is_carry = False

    for a_place, b_place in zip(a[::-1], b[::-1]):
        sum_place = int(a_place) + int(b_place)

        if is_carry:
            sum_place += 1
        
        if 9 < sum_place:
            count += 1
            is_carry = True
        else:
            is_carry = False
    
    print(count)