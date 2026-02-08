V,L,t=((1,0),(0,1),(1,1),(1,-1)),[[0]*7 for _ in range(6)],[5]*7
for i in range(21):
    X=[*map(int,input().split())]
    for k in (0,1):
        x,y=X[k]-1,t[X[k]-1]
        t[X[k]-1]-=1
        L[y][x]=k+1
        for xv,yv in V:
            sx,sy=x-3*xv,y-3*yv
            for j in range(7):
                tx,ty=sx+j*xv,sy+j*yv
                s= s + 1 if(0<=tx<7 and 0<=ty<6 and L[ty][tx]==k+1) else 0
                if s>=4:
                    print(('sk','ji')[k],i+1)
                    quit()
print('ss')