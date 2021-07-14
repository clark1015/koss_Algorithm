n,m=map(int, input().split())
length_list=list(map(int, input().split()))
length_list.sort()

min=sum(length_list)//m
max=sum(length_list)


while min<=max:
    count=0
    mid=(min+max)//2
    for i in range(n):
        if mid<0:
            count+=1
            mid=(min+max)//2
        mid-=length_list[i]
    
    if count>=3:
        min=mid+1
    
    elif count<3:
        max=mid-1

print(mid)






