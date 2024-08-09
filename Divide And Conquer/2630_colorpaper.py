n=int(input())
paper=[list(map(int, input().split())) for _ in range(n)]

colorcnt=0
whitecnt=0

def divide(rs, cs, re, ce):
    global colorcnt
    global whitecnt
    r=re-rs
    c=ce-cs
    if r==0 and c==0:
        if paper[rs][cs]==1:
            colorcnt+=1
        else:
            whitecnt+=1
        return

    iscolor=True
    iswhite=True
    for i in range(r):
        for j in range(c):
            if paper[i+rs][j+cs]==0:
                iscolor=False
            else:
                iswhite=False

    if iscolor:
        colorcnt+=1
        return
    
    if iswhite:
        whitecnt+=1
        return
    
    divide(rs, cs, rs+r//2, cs+c//2)
    divide(rs+r//2, cs+c//2, re, ce)
    divide(rs+r//2, cs, re, cs+c//2)
    divide(rs, cs+c//2, rs+r//2, ce)


divide(0,0, n, n)
print(whitecnt)
print(colorcnt)