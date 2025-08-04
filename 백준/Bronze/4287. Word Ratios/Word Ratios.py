import sys

def calc_char_distance(char_1, char_2):
    distance = 0

    char_1_index = ord(char_1)
    char_2_index = ord(char_2)

    if char_1_index <= char_2_index:
        distance = char_2_index - char_1_index
    else:
        distance = ord('z') - char_1_index + char_2_index - ord('a') + 1

    return distance

def matched_char(char, distance):
    char_code = ord(char) + distance

    if ord('z') < char_code:
        char_code = (char_code % ord('z')) + ord('a') - 1
    
    return chr(char_code)

while True:
    line = sys.stdin.readline().rstrip()

    if line == '#':
        break
    
    word_1, word_2, word_3 = line.split()

    distance_list = [0] * len(word_1)

    for i, (c1, c2) in enumerate(zip(list(word_1), list(word_2))):
        distance_list[i] = calc_char_distance(c1, c2)
    
    formatted_word = ''

    for j, c in enumerate(word_3):
        formatted_word += matched_char(c, distance_list[j])
    
    print(f'{word_1} {word_2} {word_3} {formatted_word}')