def bin_num(num):
    if num>0:
        bin_num(num//2)
        print(num%2, end='')

if __name__=="__main__":
    n=int(input())
    bin_num(n)