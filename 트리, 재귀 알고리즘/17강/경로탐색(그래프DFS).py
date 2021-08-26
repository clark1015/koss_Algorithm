def DFS(s):
    global cnt
    if s==n:
        cnt+=1
        for c in path:
            print(c, end=' ')
        print()
    else:
        
        for i in range(1,n+1):
            if g[s][i]==1 and ch[i]==0:
                ch[i]=1
                path.append(i)
                DFS(i)
                path.pop()
                ch[i]=0

if __name__=="__main__":
    n,m=map(int,input().split())
    g=[[0]*(n+1) for _ in range(n+1)]
    for i in range(m):
        a,b=map(int,input().split())
        g[a][b]=1
    ch=[0]*(n+1)
    ch[1]=1
    cnt=0
    path=[]
    path.append(1)
    DFS(1)
    print(cnt)
