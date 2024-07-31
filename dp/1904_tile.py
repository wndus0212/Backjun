n=int(input())

dp_0=1
dp_1=1
ans=0

if n==1:
    print(1)
else:
    for i in range(2,n+1):
        ans=((dp_0%15746)+(dp_1%15746))%15746
        dp_0=dp_1%15746
        dp_1=ans
    print(ans)
#(a + b) % c == (a % c + b % c) %  c