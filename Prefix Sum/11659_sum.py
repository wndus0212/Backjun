import sys

n, m= map(int, input().split())
arr= [0]+list(map(int, sys.stdin.readline().split()))
pref=[0 for _ in range(n+1)]
pref[1]=arr[1]

for i in range(2,n+1):
    pref[i]=pref[i-1]+arr[i]

for i in range(m):
    s, e= map(int, sys.stdin.readline().split())
    print(pref[e]-pref[s-1])