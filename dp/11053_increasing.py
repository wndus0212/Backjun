n=int(input())
arr=list(map(int, input().split()))
dp=[0 for _ in range(n)]

dp[0]=1

for i in range(1, n):
    maxlen=0
    for j in range(i):
        if arr[j]<arr[i] and dp[j]>maxlen:
            maxlen=dp[j]

    dp[i]=maxlen+1

print(max(dp[:n]))