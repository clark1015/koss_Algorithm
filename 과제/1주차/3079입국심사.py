import sys

def count(time: int):
    cnt:int=0
    for i in range(n):
        cnt+=time//T[i]

    return cnt

n,m=map(int, sys.stdin.readline().split())
T = [int(sys.stdin.readline()) for p in range(n)]    

lt: int=1
rt: int=max(T)*m

while lt<=rt:
    mid: int=(lt+rt)//2
    if count(mid)>=m:
        res: int=mid
        rt=mid-1
    else:
        lt=mid+1
print(res)