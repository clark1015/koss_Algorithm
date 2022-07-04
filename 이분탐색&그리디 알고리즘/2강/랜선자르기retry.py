

n ,k = map(int, input().split())
line = []

def count(mid):
    res = 0
    for i in line:
        res += i//mid
    return res

length_sum = 0
for i in range(n):
    length = int(input())
    line.append(length)
    length_sum += length
lt = 0
rt = length_sum // k

res = 0
while lt <= rt:
    mid = (lt+rt) // 2
    if count(mid) == k:
        res = mid
        lt = mid+1
    elif count(mid) > k:
        lt = mid + 1
    else:
        rt = mid - 1
print(res)
