
if __name__=="__main__":
    n=int(input()) #동전 종류 개수
    coin_list=list(map(int, input().split()))
    m=int(input()) #거스름돈 액수
    cnt=0
    for i in range(1,n+1):
        cnt+=m//coin_list[-i]
        m=m%coin_list[-i]
        if m==0:
            break

print(cnt)