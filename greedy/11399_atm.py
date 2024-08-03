n=int(input())
arr=list(map(int, input().split()))

arr.sort()

waitsum=0
wait=0
cur=0
for a in arr:
    wait=wait+a
    waitsum=waitsum+wait
    cur=cur+a

print(waitsum)