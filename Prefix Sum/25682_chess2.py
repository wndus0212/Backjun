import sys

n, m, k=map(int, input().rstrip().split())
grid=[list(sys.stdin.readline().rstrip()) for _ in range(n)]
dp=[[0 for _ in range(m)] for _ in range(n)]
