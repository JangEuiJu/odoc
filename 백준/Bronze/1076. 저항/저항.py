value_dict = {'black' : 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}

a = input()
b = input()
c = input()

answer = str(value_dict[a]) + str(value_dict[b]) 
answer = int(answer) * (10 ** value_dict[c])

print(answer)