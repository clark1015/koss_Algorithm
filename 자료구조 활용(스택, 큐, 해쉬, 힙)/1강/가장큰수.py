num, del_count=map(int,input().split())
num_list=[]

for i in str(num):
    num_list.append(int(i))

while True:
    for j in range(len(num_list)-1):
        if del_count==0:
            break
        if num_list[j]<num_list[j+1]:
            del num_list[j]
            del_count-=1
    
    if del_count!=0:
        for j in range(del_count):
            num_list.pop()
        break

print(num_list)