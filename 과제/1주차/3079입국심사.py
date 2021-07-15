def count(time):
    cnt=0
    for i in range(n):
        cnt+=time//T[i]

    return cnt
T=[]    
n,m=map(int, input().split())
for p in range(n):
    k=int(input())
    T.append(k)

lt=1
rt=max(T)*m

while lt<=rt:
    mid=(lt+rt)//2
    if count(mid)>=m:
        res=mid
        rt=mid-1
    else:
        lt=mid+1
print(res)