import sys
from collections import deque

input=sys.stdin.readline

class Que:
    def __init__(self):
        self.list=deque()
    def push(self, num):
        self.list.append(num)
    def pop(self):
        if self.list:
            pop_num=self.list[0]
            self.list.popleft()
            return pop_num
        else:
            return -1
    def size(self):
        return len(self.list)
    def empty(self):
        if self.list:
            return 0
        else:
            return 1
    def front(self):
        if self.list:
            return self.list[0]
        else:
            return -1
    def back(self):
        if self.list:
            return self.list[-1]
        else:
            return -1

n=int(input())
dq=Que()
for i in range(n):
    command=input().split()
    if command[0]=="push":
        dq.push(int(command[1]))

    elif command[0]=="pop":
        print(dq.pop())

    elif command[0]=="size":
        print(dq.size())

    elif command[0]=="empty":
        print(dq.empty())

    elif command[0]=="front":
        print(dq.front())

    elif command[0]=="back":
        print(dq.back())
