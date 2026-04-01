if __name__ == '__main__':
    n = int(input())
    nums = [1 for num in range(n) if int(input()) % 2 == 1]
    print(len(nums))
