def pal (n):
    m=str(n)
    o=m[::-1]
    if n==int(o):
        return True
    else:
        return False
a=int(input())
b=int(input())
c=[]
for i in range(a,b+1):
    if pal(i):
        c.append(i)
print(*c)
    