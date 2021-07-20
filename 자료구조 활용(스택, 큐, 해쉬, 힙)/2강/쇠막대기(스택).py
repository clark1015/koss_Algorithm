n=input()
bracket=[]
for i in n:
    bracket.append(i)
stack=[]
sum=0
for j in range(len(bracket)):
    if bracket[j]==")":
        if stack and bracket[j-1]=="(":
            stack.pop()
            sum+=len(stack)
            
        elif bracket[j-1]==")":
            stack.pop()
            sum+=1
    else:
        stack.append(bracket[j])

print(sum)