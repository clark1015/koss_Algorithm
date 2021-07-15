n,m,l=map(int, input().split())
rest_area=list(map(int, input().split()))
rest_area.append(0)
rest_area.append(l)
rest_area.sort()

def count(len):
    cnt=0
    for i in range(1,n+2):
        cnt+=(rest_area[i]-rest_area[i-1]-1)//len
    return cnt

lt=1
rt=l

while lt<=rt:
    mid=(lt+rt)//2
    if count(mid)<=m:
        res=mid
        rt=mid-1
    
    else:
        lt=mid+1
    
    
print(res)

