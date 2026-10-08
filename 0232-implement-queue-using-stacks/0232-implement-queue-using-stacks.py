class MyQueue(object):

    def __init__(self):
        self.inbox=[] 
        self.outbox=[]
        

    def push(self, x):
        self.inbox.append(x)

    def move(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        

    def pop(self):
        self.move()
        return self.outbox.pop()
        
    def peek(self):
        self.move()
        return self.outbox[-1]
        

    def empty(self):
        if not self.inbox and not self.outbox:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()