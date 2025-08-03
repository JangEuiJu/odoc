def note(i):                
    global ans
    for j in range(w*i,w*(i+1)):
        for k in range(h):      
            if s[k][j]!='?':   
                ans+=s[k][j]
                return
    ans+='?'         
    return
            
n,h,w=map(int,input().split())
s=[list(input()) for _ in range(h)]
ans=''                       
for i in range(n):
    note(i)
print(ans)
