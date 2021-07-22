a=input()
stack=[]
res=0
for i in a:
    if i.isdecimal():
        stack.append(i)
    else:
        if i=="+":
            res+=int(stack[-1])+int(stack[-2])
            for i in range(2):
                stack.pop()
            stack.append(res)
            res=0
        elif i=="-":
            res+=int(stack[-2])-int(stack[-1])
            for i in range(2):
                stack.pop()
            stack.append(res)
            res=0
        elif i=="*":
            res+=int(stack[-1])*int(stack[-2]) 
            for i in range(2):
                stack.pop()
            stack.append(res)
            res=0
        elif i=="/":
            res+=int(stack[-2])/int(stack[-1])
            for i in range(2):
                stack.pop()
            stack.append(res)
            res=0

res=''.join(map(str,stack))
print(res)