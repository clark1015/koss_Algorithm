n,m=map(int,input().split())
g=[[0]*(n+1) for _ in range(n+1)]
for k in range(m):
    a,b,r=map(int,input().split())
    g[a][b]=r

for i in range(1,n+1):
    for j in range(1,n+1):
        print(g[i][j], end=" ")
    print()
    