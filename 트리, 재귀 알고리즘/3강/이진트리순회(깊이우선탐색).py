def DFS(v):
    if v>7:
        return
    else:
        print(v,end=" ")
        DFS(v*2)
        DFS(v*2+1)
#print위치에 따라 전위 중위 후위가 됨

if __name__=="__main__":
    DFS(1)