n=int(input())
height=list(map(int,input().split()))
tower_count=len(height)

for i in range(1,len(height)+1):
    for j in range(1,i):
        if i!=1 and height[-tower_count+j-1]>height[i]:
            print(j, end=' ' )
            break
        else:
            print(0, end=' ')

