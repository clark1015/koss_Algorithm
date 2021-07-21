n=int(input())
stack=[]
for i in range(n):
    stack.clear()
    bracket=input()
    for j in range(len(bracket)):
        if bracket[j]=="(":
            stack.append(bracket[j])
        else:
            if stack and stack[-1]=="(":
                stack.pop()
            else:
                stack.append(bracket[j])
    if stack:
        print("NO")
    else:
        print("YES")
    