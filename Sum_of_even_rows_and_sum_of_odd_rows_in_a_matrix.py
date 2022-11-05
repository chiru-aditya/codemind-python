a,b=map(int,input().split())
c=[]
for i in range(a):
    x=list(map(int,input().split()))
    c.append(x)
d=s=0
for i in range(a):
    if (i%2==0):
        d+=sum(c[i])
    else:
        s+=sum(c[i])
a=list((d,s))
print(*a)
                