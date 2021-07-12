## 1주차
### 강의
4.1 회문 문자열 검사

내 풀이(파이썬)
'''python

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


        
'''
    
    

a.reverse 함수 사용시 복사본 원본 모두 순서가 바뀜
-->[::-1] 이용시 해당 리스트만 순서가 거꾸로 변경되고 원본은 유지됨

b.리스트에 문자열을 순서대로 집어넣고 리스트의 순서를 반대로 바꿔서 그 두 리스트를 비교하는 풀이를 사용함


강의 풀이
''' python

    n=int(input("n의 값을 입력하시오"))
    for i in range(n):
        s=input()
        s=s.upper()
        size=len(s)
        for j in range(size//2):
            if s[j]!=s[-1-j]:
                print("#%d NO" %(i+1))
                break
        else:
            print("#%d YES" %(i+1))
        
'''
