def f(word):
    n =["a", "e", 'i', "o", "u"]
    ans = 1
    
    check = 1 if word[0] in n else 0
    
    for w in word[1:]:
        if w in n:
            check += 1
        else:
            check -= 1
            
        if check > 1 or check < 0:
            ans = 0
            break
            
    return ans

if __name__ == "__main__":
    w = input()
    
    print(f(w))