def sol(m, k):
    if m % k == 0:
        return "Yes"
    else:
        return "No"
 
 
if __name__ == '__main__':
    m, k = map(int, input().split())
    print(sol(m, k))