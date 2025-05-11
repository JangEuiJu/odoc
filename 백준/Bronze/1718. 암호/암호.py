t, k = input(), input()

a = ''

for i in range(len(t)):
    if t[i] == ' ': a += ' '
    else: a += chr((ord(t[i]) - ord(k[i%len(k)]) - 1) % 26 + ord('a'))

print(a)