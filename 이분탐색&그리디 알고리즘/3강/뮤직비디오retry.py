import sys

n, m = map(int, sys.stdin.readline().split())
music_list = list(map(int, sys.stdin.readline().split()))

def cd_count(target):
    tmp = target
    count = 0
    for i in music_list:
        if tmp-i > 0:
            tmp -= i
        elif tmp-i == 0:
            count += 1
            tmp -= i
        else:
            count += 1
            tmp = target
            tmp -= i
    if tmp > 0:
        return count + 1
    return count


lt = 0
rt = sum(music_list)

while lt <= rt:
    mid = (lt+rt) // 2
    if cd_count(mid) == m:
        res = mid
        rt = mid-1
    elif cd_count(mid) > m:
        lt = mid + 1
    else:
        rt = mid-1
print(res)



