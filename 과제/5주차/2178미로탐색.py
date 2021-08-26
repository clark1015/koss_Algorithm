def DFS(y,x):
    global cnt, res
    if y==(n-1) and x==(m-1):
        if cnt<res:
            res=cnt
    else:
        if 0<y<n-1 and 0<x<m-1 and maze[y][x+1]==1:
            cnt+=1
            DFS(y,x+1)
        elif 0<y<n-1 and 0<x<m-1 and maze[y][x-1]==1:
            cnt+=1
            DFS(y,x-1)
        elif 0<y<n-1 and 0<x<m-1 and maze[y+1][x]==1:
            cnt+=1
            DFS(y+1,x)
        elif 0<y<n-1 and 0<x<m-1 and maze[y-1][x]==1:
            cnt+=1
            DFS(y-1,x)

if __name__=="__main__":
    n,m=map(int, input().split())
    maze=[]
    for i in range(n):
        num_list=list(map(int,input().split()))
        maze.append(num_list)
    res=2147000
    cnt=1
    print(maze)
    DFS(0,0)
    print(res)