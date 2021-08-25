def DFS(v):
    global cnt
    if v==m:
        cnt+=1
        for j in range(m):
            print(res[j], end=' ')
        print()
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                res[v]=i
                DFS(v+1)
                ch[i]=0

if __name__=="__main__":
    n,m=map(int, input().split())
    cnt=0
    ch=[0]*(n+1)
    res=[0]*n
    DFS(0)
    print(cnt)