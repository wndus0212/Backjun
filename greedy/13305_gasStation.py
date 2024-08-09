n=int(input())
dist=[0]+list(map(int, input().split()))
cost=list(map(int, input().split()))

curcost=cost[0]
totalcost=0
for i in range(1, n):
    totalcost+=curcost*dist[i]
    if cost[i]<curcost:
        curcost=cost[i]

print(totalcost)
