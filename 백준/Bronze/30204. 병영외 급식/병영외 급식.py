N, X = map(int, input().split())
A = list(input().split())

sum = 0;

for i in A :
    sum += int(i);

if sum % X == 0 :
    print(1)
else :
    print(0)