n=int(input())
dp=[0 for _ in range(101)]
dp[1]=1
dp[2]=1
dp[3]=1
dp[4]=2
dp[5]=2

ans=[]
for i in range(6, 101):
    dp[i]=dp[i-5]+dp[i-1]

for _ in range(n):
    n=int(input())
    ans.append(dp[n])   

for i in ans:
    print(i)