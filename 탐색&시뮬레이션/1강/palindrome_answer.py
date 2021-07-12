n=int(input("n의 값을 입력하시오")) #단어의 개수를 알려줌
for i in range(n):
    s=input()
    s=s.upper()
    size=len(s)
    for j in range(size//2):
        #이 부분에 주목-->문자열의 개수가 
        #홀수일 경우에 그냥 가운데 문자는 무시하면 됨!
        #이를 코드로 표현한 것이 size//2
        if s[j]!=s[-1-j]:
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))

    #for-else문은 for문이 break 없이 모두 수행되었을 경우에 
    #실행되는 코드!