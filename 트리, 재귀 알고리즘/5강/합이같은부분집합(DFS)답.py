import sys

def DFS(L, sum):
    if sum>total//2:
        return
    #합계가 토탇//2보다 커지면 더 이상 함수를 돌리는 의미가 없기에 여기서 커트한다
    #-->시간 복잡도 줄이기 위해서
    if L==n:
        if sum==(total-sum):
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)

if __name__=="__main__":
    n=int(input())
    a=list(map(int, input().split()))
    total=sum(a)
    DFS(0,0)
    print("NO")