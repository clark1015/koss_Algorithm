word=input()
bomb=input()
stack=[]

for i in range(len(word)):
    if stack[-1]==bomb[0]:
        for j in range(1,len(bomb)):
            if stack[-j]==bomb[-j]:
                sta