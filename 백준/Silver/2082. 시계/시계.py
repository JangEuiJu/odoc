correct_diode_list = [
    '####.##.##.####',
    '..#..#..#..#..#',
    '###..#####..###',
    '###..####..####',
    '#.##.####..#..#',
    '####..###..####',
    '####..####.####',
    '###..#..#..#..#',
    '####.#####.####',
    '####.####..####',
]
error_diode_list = ['' for _ in range(4)]

for _ in range(5):
    line = input().split()

    for i in range(4):
        error_diode_list[i] += line[i]

time = ''

for error_diode in error_diode_list:

    for number, correct_diode in enumerate(correct_diode_list):
        is_valid = True
        
        for ed, cd in zip(error_diode, correct_diode):
            
            if ed == '#' and cd == '.':
                is_valid = False
                break
        
        if is_valid:
            time += str(number)
            break

formatted_time = time[:2] + ':' + time[2:]

print(formatted_time)