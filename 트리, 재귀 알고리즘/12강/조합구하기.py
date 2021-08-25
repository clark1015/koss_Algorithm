def DFS(L, s):
    global cnt
    if L==m:
        for j in res:
            print(j, end=' ')
        cnt+=1
        print()
    else:
        for i in range(s,n+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=i
                DFS(L+1,i+1) #s+1이 아니라 i+1임
                ch[i]=0

if __name__=="__main__":
    cnt=0
    n,m=map(int, input().split())
    ch=[0]*(n+1)
    res=[0]*m
    DFS(0, 1)
    print(cnt)