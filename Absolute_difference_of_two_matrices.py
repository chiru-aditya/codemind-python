n=int(input())
c=[]
for i in range(n):
    x=list(map(int,input().split()))
    c.append(x)

d=[]
for i in range(n):
    x=list(map(int,input().split()))
    d.append(x)
e=[]
z=0
for i in range(n):
    h=[]
    for j in range(n):
        h.append(abs(c[i][j]-d[i][j]))
    e.append(h)
for i in e:
    print(*i)
    