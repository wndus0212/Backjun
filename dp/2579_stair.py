n=int(input())
arr=[0]+[int(input()) for _ in range(n)]
dp=[0 for _ in range(n+1)]

if n==1:
    print(arr[1])
elif n==2:
    print(arr[1]+arr[2])
else:
    dp[1]=arr[1]
    dp[2]=arr[1]+arr[2]
    for i in range(3, n+1):
        #1. 2칸 전을 밟고 옴. 2. 3칸 전과 1칸 전을 밟고 옴
        dp[i]=max(dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i])

    print(dp[n])