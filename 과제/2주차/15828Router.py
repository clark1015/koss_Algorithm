from collections import deque
import sys
input=sys.stdin.readline

storage=int(input())
buffer=deque()
n=0
while n!=-1:
    n=int(input())
    if n==0:
        buffer.popleft()
    else:
        if len(buffer)<storage:
            if n!=-1:
                buffer.append(n)
        else:
            pass

if buffer:
    for i in buffer:
        print(i, end=' ')

else:
    print("empty")