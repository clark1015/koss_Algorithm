import sys
from collections import deque

def DFS(L, sum, tsum):
    global result
    if sum+(total-tsum)<result:
        return
    if sum>c:
        return
    if L==n: #부분집합이 하나 완성되는 지점
        if sum>result:
            result=sum

    else:
        DFS(L+1, sum+a[L], tsum+a[L])
        DFS(L+1, sum, tsum+a[L])

if __name__=="__main__":
    c,n=map(int, input().split())
    a=[0]*n
    result=-2147000000
    for i in range(n):
        a[i]=int(input())
        total=sum(a)
    DFS(0, 0, 0)
    print(result)