def DFS():
    global a
    a=a+[4]
    print(a)

if __name__=="__main__":
    a=[1,2,3]
    DFS()
    print(a)