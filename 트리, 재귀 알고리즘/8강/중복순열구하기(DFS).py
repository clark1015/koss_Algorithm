def DFS(v):
	if v<=n:
		for i in range(1,n+1):
			for j in range(m-1):
				print(v, i)
    

if __name__=="__main__":
    n, m=map(int, input().split())
    num_list=[]
    for i in range(1,n+1):
        DFS(i)
    print(n**m)