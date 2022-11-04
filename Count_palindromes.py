def pal(a):
    c=str(a)
    b=c[::-1]
    d=int(b)
    if a==d:
        return True
    return False
n=int(input())
a=list(map(int,input().split()))
m=0
for i in a:
    if pal(i):
        m+=1
print(m)        
        
        