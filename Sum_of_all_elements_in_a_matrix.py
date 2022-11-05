a,b=map(int,input().split())
l=[]
for i in range(a):
    x=list(map(int,input().split()))
    l.append(x)
s=0
for i in range(len(l)):
    s+=sum(l[i])
print(s)    
          