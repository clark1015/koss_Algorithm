import sys
from collections import deque

def DFS(L, sum, tsum):
    global result
    if sum+(total-tsum)<result:
        #시간 초과를 해결하기 위한 코드
        #불필요한 지점 커팅 코드
        #여태까지의 sum(합계)에서 나머지 노드들을 모두 더해도 
        #result값보다 작다면 더이상의 계산은 불필요하기에 cut
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