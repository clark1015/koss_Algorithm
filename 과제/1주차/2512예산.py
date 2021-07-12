n=int(input())
budget_list=list(map(int, input().split()))
budget_sum=int(input())

if budget_sum<sum(budget_list):
    standard_budget=budget_sum/n
    out_range=0
    for i in range(len(budget_list)):
        if budget_list[i]<=standard_budget:
            budget_sum-=budget_list[i]
        else:
            out_range+=1

    print(budget_sum//out_range)
    
else:
    print(max(budget_list))