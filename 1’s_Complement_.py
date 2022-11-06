n=int(input())
n=bin(n)
n=n[2:]
n=list(n)
for i in range(len(n)):
    if n[i]=="0":
        n[i]=1
    else:
        n[i]=0
s=0
t=len(n)
for i in n:
    t=t-1
    s+=i*2**t
print(s)