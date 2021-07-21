a=input()
stack=[]
res=''

for i in a:
    if i.isdecimal():
        res+=i
    else:
        if i=="+" or i=="-":
            if stack and (stack[-1]=="*" or stack[-1]=="/"):
                res+=stack.pop()
                stack.append(i)
            else:
                stack.append(i)

        elif i=="(":
            stack.append(i)
        
        elif i==")":
            while stack[-1]!="(":
                res+=stack.pop()
            stack.pop()
        
        elif i=="*" or i=="/":
            if stack and (stack[-1]== "*" or stack[-1]=="/"):
                res+=stack.pop()
                stack.append(i)
            else:
                stack.append(i)

if stack:
    while len(stack)!=0:
        res+=stack.pop()

print(res)

            
