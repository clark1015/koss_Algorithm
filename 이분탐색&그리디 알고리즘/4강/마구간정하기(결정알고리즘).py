n, c =map(int, input().split())
position_list=[]
result_list=[]

def position(length):
    for j in position_list:
        if position_list[0]<=j-length and j+length<=position_list[len(position_list)]:
            result_list.append(j)
    return result_list
            
for i in range(n):
    p=int(input())
    position_list.append(p)

position_list.sort() 

lt=1
rt=max(position_list)

while lt<=rt:
    mid=(lt+rt)//2
    if len(position(mid))>0:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
