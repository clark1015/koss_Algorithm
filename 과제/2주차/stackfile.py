
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
        