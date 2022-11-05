n=int(input())
d=n
s=[]
while n:
    r=n%10
    s.append(r)
    n=n//10
a=len(s)
c=s[::-1]
b=0
for i in range(a,0,-1):
    b+=c[i-1]**(i)
if d==b:
    print("True")
else:
    print("False")
