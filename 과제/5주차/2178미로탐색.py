def DFS(y,x):
    global cnt,res
    if 
    else:
        if 0<y<n-1 and 0<x<m-1 and maze[y][x+1]==1:
            cnt+=1
            maze[y][x]=0
            DFS(y,x+1)
            maze[y][x]=1
        elif 0<y<n-1 and 0<x<m-1 and maze[y][x-1]==1:
            cnt+=1
            maze[y][x]=0
            DFS(y,x-1)
            maze[y][x]=1
        elif 0<y<n-1 and 0<x<m-1 and maze[y+1][x]==1:
            cnt+=1
            maze[y][x]=0
            DFS(y+1,x)
            maze[y][x]=1
        elif 0<y<n-1 and 0<x<m-1 and maze[y-1][x]==1:
            cnt+=1
            maze[y][x]=0
            DFS(y-1,x)
            maze[y][x]=1
        
    print(res)

if __name__=="__main__":
    n,m=map(int, input().split())
    maze=[]
    for i in range(n):
        num_list=list(map(int,input().split()))
        maze.append(num_list)
    cnt=1
    d=[(-1,0),(1,0),(0,-1),(0,1)]
    print(maze)
    res=2147000000
    DFS(0,0)
    