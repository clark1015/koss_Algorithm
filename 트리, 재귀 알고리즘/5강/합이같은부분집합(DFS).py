import sys

def DFS(v):
    list=[]
    result="NO"
    if v==n:
        for i in range(n):
            if ch[i]==1:
                list.append(num_set[i])
        if 2*sum(list)==sum(num_set):
            result="YES"
            print(result)
            sys.exit(0)
            return
        
    else:
        ch[v]=1
        DFS(v+1)
        ch[v]=0
        DFS(v+1)
    


if __name__=="__main__":
    n=int(input())
    num_set=list(map(int,input().split()))
    ch=[0]*n
    DFS(0)
    print("NO")