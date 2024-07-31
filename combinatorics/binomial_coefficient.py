n, k = map(int, input().split())

def combination(a):
    if a==1 or a==0:
        return 1
    return a*combination(a-1)

def bc(n, k):
    return combination(n)//(combination(n-k)*combination(k))

print(bc(n, k))