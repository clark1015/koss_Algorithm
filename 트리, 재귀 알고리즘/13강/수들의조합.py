def DFS(L):
    global cnt
    if L==k and sum(res)%m==0:
        print(res)
        print()
    elif L!=k:
        for i in range(1, n+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=num_list[i-1]
                DFS(L+1)
                ch[i]=0
                res.sort()
if __name__=="__main__":
    n,k=map(int, input().split())
    num_list=list(map(int,input().split()))
    m=int(input())
    cnt=0
    ch=[0]*(n+1)
    res=[0]*k
    DFS(0)
   