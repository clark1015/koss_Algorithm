k, n = map(int, input().split())
length_list=[]
for i in range(k):
    p=int(input())
    length_list.append(p)

lt=1
rt=max(length_list)
res=0

while lt<=rt:
    mid=(lt + rt)//2
    lan_count=0
    for j in range(k):
        lan_count += length_list[j]//mid
    
    if lan_count<n:
        rt=mid-1
    elif lan_count>=n:
        res=mid
        lt=mid+1

print(res)
