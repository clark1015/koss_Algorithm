n= int(input("n의 값을 입력하시오"))
for i in range(n):
    s=input()
    s.upper()
    size=len(s)
    for j in range(size//2): #이 부분에 주목-->문자열의 개수가 홀수일 경우에 그냥 가운데 문자는 무시하면 됨!
        if s[j]!=s[-1-j]:
            print("NO")
            break
    else:
        print("yes")
