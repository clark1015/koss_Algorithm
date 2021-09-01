n=int(input())
height=list(map(int,input().split()))
tower_count=len(height)

for i in range(len(height)):
    for j in range(i):
        if j!=0 and height[-tower_count+j]>height[i]:
            print(len(height)+1-tower_count+j, end=' ' )
            break
        else:
            print(0, end=' ')

