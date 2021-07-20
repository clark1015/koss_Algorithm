import sys

input=sys.stdin.readline

class Stack:
    def __init__(self):
        self.list=[]

    def push(self, num):
        self.list.append(num)

    def pop(self):
        if self.list:
            pop_num=self.list[-1]
            self.list = self.list[:-1]
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

    def top(self):
        if len(self.list)>0:
            return self.list[-1]
        else:
            return -1
        

num=int(input())
stack=Stack()
for i in range(num):
    input_split=input().split()

    if input_split[0]=="push":
        stack.push(input_split[1])
    elif input_split[0]=="pop":
        print(stack.pop())
    elif input_split[0]=="size":
        print(stack.size())
    elif input_split[0]=="empty":
        print(stack.empty())
    elif input_split[0]=="top":
        print(stack.top())