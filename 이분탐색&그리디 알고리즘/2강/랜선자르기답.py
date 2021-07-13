def count(len):
    cnt=0
    for x in Line:
        cnt+=(x//len)
    #함수 count: 랜선 개수 구하는 함수
    #cnt-->len을 길이로 지정했을 때 나오는 랜선의 개수

k,n=map(int, input().split())
Line=[]
res=0
largest=0
for i in range(k):
    tmp=int(input()) #Line 리스트에 자르기 전 랜선 길이를 입력
    Line.append(tmp)
    largest=max(largest, tmp)

lt=1
rt=largest
while lt <= rt:
    mid=(lt+rt)//2
    if count(mid)>=n:
        res=mid
        lt=mid+1

    else:
        rt=mid-1
    
print(res)