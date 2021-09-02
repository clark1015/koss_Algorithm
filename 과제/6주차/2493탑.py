n=int(input())
height=list(map(int,input().split()))
tower_count=len(height)
stack=[]
res=[]

for i in range(tower_count):
    
    while stack:
        if stack[-1][1]>height[i]:
            res.append(stack[-1][0]+1)
            break
        else:
            stack.pop()
    if not stack:
        res.append(0)

    stack.append([i,height[i]])
    

print(" ".join(map(str,res)))