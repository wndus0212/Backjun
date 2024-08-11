n= int(input())
arr=[list(map(int, input())) for _ in range(n)]

def divide(rs, cs, re, ce):
    r=re-rs
    c=ce-cs
    if r==0 and c==0:
        if arr[rs][cs]==1:
            print(1, end="")
        else:
            print(0, end="")
        return

    iscolor=True
    iswhite=True
    for i in range(r):
        for j in range(c):
            if arr[i+rs][j+cs]==0:
                iscolor=False
            else:
                iswhite=False

    if iscolor:
        print(1, end="")
        return
    
    if iswhite:
        print(0, end="")
        return
    
    print("(", end="")
    divide(rs, cs, rs+r//2, cs+c//2)
    divide(rs, cs+c//2, rs+r//2, ce)
    divide(rs+r//2, cs, re, cs+c//2)
    divide(rs+r//2, cs+c//2, re, ce) 
    
    print(")", end="")

divide(0,0,n,n)