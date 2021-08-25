def DFS(L):
    if L==N+1:
        for i in range(L):
            for j in range(n-i-1):

    else:
        for k in range(1,n+1):
            if ch[k]==0:
                ch[k]=1
                res[L]=k
                DFS(L+1)
                ch[k]=0


if __name__=="__main__":
    n,f=map(int, input().split())
    res=[0]*n
    ch=[0]*(n+1)
    DFS(0)