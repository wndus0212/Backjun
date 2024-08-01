import sys

n, k=map(int, input().split())
coin=[]

for _ in range(n):
    coin.append(int(sys.stdin.readline().rstrip()))

cnt=0
while k>0:
    maxcoin=0
    for c in coin:
        if k>=c and c>maxcoin:
            maxcoin=c
    cnt+=1
    k=k-maxcoin

print(cnt)