def DFS(y,x):
    stack=[(y,x)]
    g[y][x]=1
    num=1

    while stack:
        y,x=stack.pop()
        for dx, dy in d:
            nx,ny=x+dx,y+dy
            if nx<0 or nx>=n or ny<0 or ny>=m: 
                pass
            if g[ny][nx]==0:
                stack.append((ny,nx))
                g[ny][nx]=1
                num+=1
    print(nx,ny)
    res.append(num)

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
    d=[(-1,0), (1,0), (0,-1), (0,1)]
    res=[]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if g[i][j]==0:
                DFS(i,j)
    print(len(res))
    res.sort()
    for x in res:
        print(x, end=' ')
    
