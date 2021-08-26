import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline
def DFS(s):
    global cnt
    if ch[s]==1:
        cnt+=1
        
    else:
        ch[s]=1
        DFS(num_list[s-1])

if __name__=="__main__":
    T=int(input())
    for i in range(T):
        n=int(input())
        num_list=list(map(int, input().split()))
        ch=[0]*(n+1)
        cnt=0
        DFS(1)
        
        if 0 in ch:
            for k in range(1,n+1):
                if ch[k]==0:
                    DFS(k)
        print(cnt)