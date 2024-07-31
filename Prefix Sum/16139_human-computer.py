import string
import sys
alphabetlist=string.ascii_lowercase
inputstr=input()
inputstr=[0]+list(inputstr)
q=int(input())
cnt=[[0 for _ in range(26)] for _ in range(len(inputstr))]

for i in range(1, len(inputstr)):
    for a in alphabetlist:
        if inputstr[i]==a:
            for j in range(26):
                cnt[i][j]=cnt[i-1][j]

            cnt[i][alphabetlist.index(a)]+=1

for _ in range(q):
    alphabet, s, e=sys.stdin.readline().split()
    s=int(s)
    e=int(e)
    result=cnt[e+1][alphabetlist.index(alphabet)]-cnt[s][alphabetlist.index(alphabet)]
    sys.stdout.write(str(result)+"\n")