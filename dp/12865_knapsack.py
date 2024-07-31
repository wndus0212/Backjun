n, k=map(int, input().split())
bag=[[0, 0] for _ in range(n+1)]
dp=[[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    weight, value=map(int, input().split())
    bag[i][0]=weight
    bag[i][1]=value

for i in range(1, n+1):
    for j in range(1, k+1):
        if j>=bag[i][0]:
            dp[i][j]=max(dp[i-1][j], dp[i-1][j-bag[i][0]]+bag[i][1])
        else:
            dp[i][j]=dp[i-1][j]

print(dp[-1][-1])