def pal(a):
    c=str(a)
    b=c[::-1]
    d=int(b)
    return d
    
n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    c.append(pal(i))
print(*c)        
    