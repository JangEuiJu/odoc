import sys

number_list = list(range(2, 10007 + 1))
prime_list = []

while len(number_list) != 0:
    prime = number_list[0]
    prime_list.append(prime)

    for i in range(prime, 10007 + 1, prime):
        if i in number_list:
            number_list.remove(i)

n = int(sys.stdin.readline())

for i in range(n):
    v = int(sys.stdin.readline())

    print(f'Input value: {v}')

    if v in prime_list:
        print('Would you believe it; it is a prime!')
    else:
        diff = 10007

        for p in prime_list:
            if abs(p - v) < diff:
                diff = abs(p - v)

        print(f'Missed it by that much ({diff})!')

    if i != n - 1:
        print()