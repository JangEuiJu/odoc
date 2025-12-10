import sys
input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]

m = int(input())
check_word = [input().strip() for _ in range(m)]

idx = words.index("?")

pre = words[idx - 1] if idx > 0 else ""
post = words[idx + 1] if idx < n - 1 else ""

for w in check_word:
    if w not in words:
        if (pre == "" or w[0] == pre[-1]) and (post == "" or w[-1] == post[0]):
            print(w)
            break