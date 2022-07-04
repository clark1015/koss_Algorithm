n, m =map(int, input().split())
num_list=list(map(int, input().split()))
num_list.sort()

lt=0
rt=len(num_list)

while True:
    mid=(lt+rt)//2
    if num_list[mid]<m:
        lt=mid+1
    
    elif num_list[mid]>m:
        rt=mid-1

    elif num_list[mid]==m:
        print("wowowo " ,num_list[mid])
        print(mid+1)
        break
