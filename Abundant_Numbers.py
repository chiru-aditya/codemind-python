n=int(input())
s=[]
for i in range(1,n):
    if n%i==0:
        s.append(i)
c=0
for i in s:
    c+=i
if c>n:
    print("True")
else:
    print("False")
    
