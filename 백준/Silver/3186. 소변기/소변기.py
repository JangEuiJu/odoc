import re

k, l, n = map(int, input().split())
s = input()
arr = [st.end() - 1 for st in re.finditer('1' * k, s)]
ans = []
if len(arr) == 0:
    print("NIKAD")
    exit()

for i in range(len(arr) - 1):
    if s[arr[i] + 1: arr[i + 1]].find('0' * l) != -1:
        ans.append(s[arr[i] + 1: arr[i + 1]].find('0' * l) + l + arr[i] + 1)

if s[arr[len(arr) - 1] + 1:].find('0' * l) != -1:
    ans.append(s[arr[len(arr) - 1] + 1:].find('0' * l) + l + arr[len(arr) - 1] + 1)
else:
    ans.append(s.rfind('1') + 1 + l)

for a in ans:
    print(a)