def DFS(v, sum):
    global result
    if result<v:
        return
    if sum==m:
        if result>v:
            result=v
    elif sum>m:
        return
    
    else:
        for i in range(n):
            DFS(v+1, sum+coin_list[i])
if __name__=="__main__":
    result=2147000000
    n=int(input())
    coin_list=list(map(int, input().split()))
    coin_list.reverse()
    m=int(input())
    DFS(0, 0)
    print(result)