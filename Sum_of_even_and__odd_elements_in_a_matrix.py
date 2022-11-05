a,b=map(int,input().split())
l=[]
for i in range(a):
    x=list(map(int,input().split()))
    l.append(x)
c=s=0
for i in range(len(l)):
    for j in range(b):
        if (l[i][j])%2==0:
            s+=(l[i][j])
        else :
            c+=(l[i][j])
d=list((s,c))
print(*d)

            