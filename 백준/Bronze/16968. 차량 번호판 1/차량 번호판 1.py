forms = {'c': 26, 'd': 10}
s = input()

answer = forms[s[0]]

for i in range(1, len(s)):
    mul = forms[s[i]]
    if s[i] == s[i - 1]:
        mul -= 1
    answer *= mul

print(answer)