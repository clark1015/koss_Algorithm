#295kg의 무게를 버틸 수 있다
#N마리의 바둑이가 무게로 표현됨
#DFS로 가능한 모든 경우를 출력해서 그의 최대 무게를 가져온다
def DFS(v):

    if v==n:
        sum=0
        for j in range(n):
            if ch[j]==1:
                sum+=weight_list[j]
        if sum<=c:
            result_list.append(sum)
              
    else:
        ch[v]=0
        DFS(v+1)
        ch[v]=1
        DFS(v+1)

if __name__=="__main__":
    result_list=[]
    weight_list=[]
    c, n=map(int, input().split())
    #리스트에 무게 집어넣고 처리하기 
    #or  각각 문자로 설정하기?
    for i in range(n):
        a=int(input())
        weight_list.append(a)
    ch=[0]*n
    DFS(0)
    print(max(result_list))
