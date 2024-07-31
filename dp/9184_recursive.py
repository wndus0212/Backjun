arr=[]

while True:
    a, b, c= map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break
    
    arr.append((a, b, c))

dp=[[[0 for _ in range(51)] for _ in range(51)] for _ in range(51)]
for i in range(51):
    for j in range(51):
        dp[i][j][0]=1
        dp[i][0][j]=1
        dp[0][i][j]=1
    

for i in range(1,21):
    for j in range(1,21):
        for k in range(1,21):      
            if a<b and b<c:
                dp[i][j][k]=dp[i][j][k-1]+dp[i][j-1][k-1]-dp[i][j-1][k]
            else:
                dp[i][j][k]=dp[i-1][j][k] + dp[i-1][j-1][k]+ dp[i-1][j][k-1] - dp[i-1][j-1][k-1]

for aa, bb, cc in arr:
    if aa<=0 or bb<=0 or cc<=0:
        print("w(",aa,", ",bb,", ",cc,") = ",1,sep="") 
    elif aa>20 or bb>20 or cc>20:
        print("w(",aa,", ",bb,", ",cc,") = ",dp[20][20][20],sep="") 
    else:
        print("w(",aa,", ",bb,", ",cc,") = ",dp[aa][bb][cc], sep="")          

