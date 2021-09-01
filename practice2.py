word=input()
bomb=input()
stack=[]

for i in word:
    if stack and stack[-1]==bomb[-1]:
        for k in range(1,len(bomb)):
            if stack[-k]==bomb[-k]:
                pass
            else:
                break
        else:
            for k in range(len(bomb)-1):
                stack.pop()
    else:
        stack.append(i)
print(stack)