import sys

lines = sys.stdin.read().split()

for line in lines:
    soundex = '0'
    before = ''
    
    for char in line:
        if char == before:
            continue
        
        if char in ['B', 'F', 'P', 'V'] and soundex[-1] != '1':
            soundex += '1'
        elif char in ['C', 'G', 'J', 'K', 'Q', 'S', 'X', 'Z'] and soundex[-1] != '2':
            soundex += '2'
        elif char in ['D', 'T'] and soundex[-1] != '3':
            soundex += '3'
        elif char in ['L'] and soundex[-1] != '4':
            soundex += '4'
        elif char in ['M', 'N'] and soundex[-1] != '5':
            soundex += '5'
        elif char in ['R'] and soundex[-1] != '6':
            soundex += '6'
        else:
            soundex += '0'
        
        before = char
    
    soundex = soundex.replace('0', '')
    
    print(soundex)