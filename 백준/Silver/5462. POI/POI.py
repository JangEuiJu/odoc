n,t,p = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)] 
r = [[0,0] for _ in range(n)]    
s = [0]*t              
 
for i in range(n):               
    for j in range(t):
        if a[i][j] == 0:   
            s[j]+=1
 
for i in range(n):                 
    for j in range(t):
        if a[i][j] == 1:
            r[i][0]+=s[j]
            r[i][1]+=1
            
k1, k2 = r[p-1][0], r[p-1][1]     
c=1                                  
for i in range(n):
    if r[i][0] > k1:                 
        c+=1
    elif r[i][0] == k1 and r[i][1] > k2:    
        c+=1
    elif r[i][0] == k1 and r[i][1] == k2 and i+1 < p:  
        c+=1
print(k1,c)
