def DFS(index, score, time):
    global res
    if time > m:
        return

    if index == n-1:
        if score > res :
            res = score

    else:
        DFS(index+1, score+pv[index], time+pt[index])
        DFS(index+1,score , time)


if __name__ == "__main__":
    n,m = map(int, input().split())
    pv = list()
    pt = list()
    for i in range(n):
        a, b = map(int, input().split())
        pv.append(a)
        pt.append(b)
    res = -100000000

    DFS(0,0,0)
    print(res)