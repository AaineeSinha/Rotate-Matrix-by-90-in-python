n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(i,n):
        a[i][j],a[j][i]=a[j][i],a[i][j]
for i in range(n):a[i].reverse()
for row in a:print(*row)
