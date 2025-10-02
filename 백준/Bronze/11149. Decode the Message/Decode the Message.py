import sys
from string import ascii_lowercase

matched_alphabat = dict(zip(range(26 + 1), list(ascii_lowercase) + [' ']))

T = int(sys.stdin.readline())

for _ in range(T):
    line = sys.stdin.readline().rstrip().split()

    decode_message = ''

    for ciphertext in line:
        base_char_code = ord('a')
        total_code_value = 0

        for char in ciphertext:
            total_code_value += ord(char) - base_char_code
        
        total_code_value %= 27

        decode_message += matched_alphabat[total_code_value]
    
    print(decode_message)