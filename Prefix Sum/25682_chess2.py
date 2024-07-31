import sys

n, m, k=map(int, input().rstrip().split())
grid=[list(sys.stdin.readline().rstrip()) for _ in range(n)]

def pref(c):
    prefix=[[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if (i+j)%2:
            #i+j가 홀수-> 왼쪽 위에 있는 색과 다른 색이 와야 함
                if grid[i-1][j-1]==c:
                    prefix[i][j]=prefix[i-1][j]+prefix[i][j-1]-prefix[i-1][j-1]+1
                else:
                    prefix[i][j]=prefix[i-1][j]+prefix[i][j-1]-prefix[i-1][j-1]
            else:
            #i+j가 짝수-> 왼쪽 위에 있는 색과 같은 색이 와야 함
                if grid[i-1][j-1]==c:
                    prefix[i][j]=prefix[i-1][j]+prefix[i][j-1]-prefix[i-1][j-1]
                else:
                    prefix[i][j]=prefix[i-1][j]+prefix[i][j-1]-prefix[i-1][j-1]+1
    ans=sys.maxsize

    for i in range(1,n-k+2):
        for j in range(1,m-k+2):
            sum=prefix[i+k-1][j+k-1]-prefix[i-1][j+k-1]-prefix[i+k-1][j-1]+prefix[i-1][j-1]
            ans=min(ans, sum)
    return ans

print(min(pref('B'), pref('W')))