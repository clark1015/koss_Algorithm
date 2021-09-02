n=int(input())
height=list(map(int,input().split()))
tower_count=len(height)
stack=[]
res=[]

for i in range(tower_count):
    k=height[i]
    stack.append(height[i])
    for j in range(-len(stack),-1):
        if stack[j]>k:
            print(tower_count+j)
            res.append(tower_count+j)
            break
    else:
        res.append(0)


print(res)