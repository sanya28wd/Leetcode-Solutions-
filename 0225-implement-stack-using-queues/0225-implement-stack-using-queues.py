class MyStack(object):

    def __init__(self):
        self.q=deque()
        self.d=deque()

    def push(self, x):
        while(len(self.q)>0):
            self.d.append(self.q.popleft())
        self.q.append(x)
        while(len(self.d)>0):
            self.q.append(self.d.popleft())


    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        if not self.q:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()