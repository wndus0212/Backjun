import sys

n=int(input())
room=[]
cnt=0
for _ in range(n):
    s, e= map(int, sys.stdin.readline().split())
    room.append((e,s))

room.sort()

curstart=0
for r in room:
    if r[1]>=curstart:
        curstart=r[0]
        cnt+=1

print(cnt)