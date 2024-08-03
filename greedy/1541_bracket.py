exp=input()
exp=list(exp)+['=']

n=0
ans=0
tmp=0
dominus=0
for c in exp:
    if c.isdigit():
        n=n*10+int(c)
    else:
        print(n)
        if c=='-':
            if dominus==0:
                ans=ans+n
                n=0
                dominus=1
            else:
                ans=ans-n
                n=0
        if c=='+':
            if dominus==1:
                ans=ans-n
                n=0
            else:
                ans=ans+n
                n=0
        else:
            if dominus==1:
                ans=ans-n
            else:
                ans=ans+n

print(ans)