def func():
    answer = 0
    
    while True:
        try:
            gum = input()
            answer += 1
        except EOFError:
            break
    
    return answer


if __name__ == "__main__":
    print(func())