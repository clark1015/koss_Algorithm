def count(capacity):
    cnt=1
    #cnt를 1로 두느냐 0으로 두느냐-->시작 포인트부터 세느냐 아니면 끝나는 포인트마다 세느냐의 차이
    #이를 루프가 끝날 때 개수가 반영되는지를 따져야 됨--만약 안되면 시작 포인트부터 세야됨
    sum=0
    for i in Music:
        if sum+i>capacity:
            sum=i
            cnt+=1
        else:
            sum+=i
    return cnt


n,m=map(int, input().split())
Music=list(map(int, input().split()))
maxx=max(Music)

lt=1
rt=sum(Music)
res=0
while lt<=rt:
    mid=(lt+rt)//2
    if mid>=maxx and count(mid)<=m:
        res=mid
        rt=mid-1
    else:
        lt=mid+1
print(res)