n=int(input())
budget_list=list(map(int, input().split()))
budget_sum=int(input())

min_budget=0
max_budget=max(budget_list)

res=0

while min_budget<=max_budget:
    num=0 
    #num=0가 루프 안에 있어야 함!!
    mid=(min_budget+max_budget)//2
    for i in range(n):
        if budget_list[i]>mid:
            num+=mid
        else:
            num+=budget_list[i]
            

    if num<=budget_sum:
        res=mid
        min_budget=mid+1
    
    else:
        max_budget=mid-1


print(res)