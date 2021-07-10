count=int(input())
string_list=[]
string_list_clone=[]

for i in range(count):
    string_list.clear()
    string_list_clone.clear()
    string=input().lower()
    
    for j in string:
        string_list.append(j)
   
    string_list_clone=string_list[::-1]

    if string_list_clone==string_list:
        print("YES")
    else:
        print("NO")

    
    
