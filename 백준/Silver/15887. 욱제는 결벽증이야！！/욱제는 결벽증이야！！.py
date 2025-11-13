n=int(input())
a=list(map(int,input().split()))
b=a.copy()
b.sort()
i=1
op=0
ch=[]
while a!=b:
    if a[i-1]!=i:
        op+=1
        k=a.index(i)+1
        a[i-1:a.index(i)+1]=a[i-1:a.index(i)+1][::-1]
        ch.append([i,k])
    i+=1
print(op)
for i in ch: print(*i)