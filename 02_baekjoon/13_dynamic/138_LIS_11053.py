import sys

n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))

d=[1 for i in range(n)]

for i in range(1,n):
    for j in range(i):
        if a[i]>a[j]:
            d[i]=max(d[i],d[j]+1)

print(max(d))

