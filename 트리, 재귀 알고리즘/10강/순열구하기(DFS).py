def DFS(L):
    global cnt
    if L==m:
        for j in range(L):
            print(res[j], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1, n+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=i
                DFS(L+1)
                ch[i]=0 #되돌아와서 초기화하는 코드

if __name__=="__main__":
    n,m=map(int, input().split()) #n은 구슬에 적힌 번호 1부터 n까지
    res=[0]*n
    ch=[0]*(n+1)
    cnt=0
    DFS(0)
    print(cnt)
