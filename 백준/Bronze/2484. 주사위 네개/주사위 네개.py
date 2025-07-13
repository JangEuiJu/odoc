n=int(input())
prizes=[]
for _ in range(n):
    prize=0
    dice=sorted(list(map(int,input().strip().split())))
    if len(set(dice))==1:
        prize=50000+5000*(dice[0])
    elif len(set(dice))==2:
        if dice[1]==dice[2]:
            prize=10000+1000*dice[1]
        else:
            prize=2000+(dice[1]+dice[2])*500
    elif len(set(dice))==4:
        prize=dice[-1]*100
    else:
        for i in range(3):
            if dice[i]==dice[i+1]:
                prize=1000+100*dice[i]
                break
    prizes.append(prize)
print(max(prizes))