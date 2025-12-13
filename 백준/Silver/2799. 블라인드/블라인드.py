import sys

M, N = map(int, sys.stdin.readline().split())

is_first = True
floor_list = [0] * N

blind_list = [0] * 5

for _ in range((5 * M) + 1):
    line = sys.stdin.readline().rstrip()

    if line == '#' * ((5 * N) + 1):
        if is_first:
            is_first = False
            continue
        
        for floor in floor_list:
            blind_list[int(floor / 4)] += 1

        floor_list = [0] * N
        continue
    
    index = 0

    for element in line.split('#'):
        if element != '':
            floor_list[index] += element.count('*')

            index += 1
    
print(*blind_list)