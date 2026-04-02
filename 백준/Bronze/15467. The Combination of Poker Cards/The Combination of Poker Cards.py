import sys

T = int(sys.stdin.readline())

for _ in range(T):
    card_list = list(map(int, sys.stdin.readline().split()))
    card_set = set(card_list)

    card_count = []

    for card in card_set:
        card_count.append(card_list.count(card))
    
    card_count.sort()

    if len(card_count) == 6:
        print('single')
    elif len(card_count) == 5:
        print('one pair')
    elif len(card_count) == 4 and max(card_count) == 3:
        print('one triple')
    elif len(card_count) == 4:
        print('two pairs')
    elif len(card_count) == 3 and max(card_count) == 4:
        print('tiki')
    elif len(card_count) == 3 and max(card_count) == 3:
        print('full house')
    elif len(card_count) == 3:
        print('three pairs')
    elif len(card_count) == 2 and max(card_count) == 4:
        print('tiki pair')
    elif len(card_count) == 2:
        print('two triples')