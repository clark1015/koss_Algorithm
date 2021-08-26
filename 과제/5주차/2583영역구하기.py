def DFS(y,x):
    global cnt
    if g[y][x]==0:
        g[y][x]=1
        cnt+=1
        if g[y][x+1]==0:
            DFS(y,x+1)
        elif g[y+1][x]==0:
            DFS(y+1,x)

            


if __name__=="__main__":
    m,n,k=map(int, input().split())
    g=[[0]*(n+1) for _ in range(m+1)]
    for k in range(k):
        x1,y1,x2,y2=map(int, input().split())
        for p in range(m-y2+1,m-y1+1):
            for q in range(x1+1,x2+1):
                if g[p][q]==0:
                    g[p][q]=1
    for i in range(1,m+1):
        for j in range(1,n+1):
            print(g[i][j], end=' ')
        print()
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cnt=1
    DFS(1,1)
    print(cnt)
