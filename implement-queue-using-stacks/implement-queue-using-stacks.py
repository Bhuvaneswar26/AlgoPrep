class MyQueue:

    def __init__(self):

        self.stack1 = list()

        self.stack2 = list()

    def push(self, x: int) -> None:

        while(self.stack1):

            pop =  self.stack1.pop()

            self.stack2.append(pop)

        self.stack2.append(x)

        while(self.stack2):

            pop =  self.stack2.pop()

            self.stack1.append(pop)


    def pop(self) -> int:

        return self.stack1.pop()

    def peek(self) -> int:
        
        return self.stack1[-1]

    def empty(self) -> bool:
        
        return  not(bool(len(self.stack1)))


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()