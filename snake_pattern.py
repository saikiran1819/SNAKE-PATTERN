### SNAKE PATTERN WITH ONE SINGLE LOOP
n=int(input('Enter a number:-'))
i=1
s=''
d=0
c=1
while i<=n**2:
    if c%2!=0:
        print(i,end='')
        d+=1
        if d==n:
            d=0
            c+=1
            print()
    else:
        t=str(i)
        t=t[-1::-1]
        s+=t
        d+=1
        if d==n:
            print(s[-1::-1])
            d=0
            c+=1
            s=''
    i+=1
