a=int(input())

if a%7==0:
    flag=1
    while a>0:
        if a%10 == 7:flag = 3
        a//=10
else:
    flag=0
    while a>0:
        if a%10 == 7:flag = 2
        a//=10
        
print(flag)