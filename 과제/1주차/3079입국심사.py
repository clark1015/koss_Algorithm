def count(time: int):
    cnt:int=0
    for i in range(n):
        cnt+=time//T[i]

    return cnt
T = []    
n,m=map(int, input().split())
for p in range(n):
    k=int(input())
    T.append(k)

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