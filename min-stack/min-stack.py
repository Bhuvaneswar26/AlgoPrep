class MinStack:

    def __init__(self):

        self.stack1 = []

        self.stack2  = []

        self.stack3 = []
        

    def push(self, val: int) -> None:

        self.stack1.append(val)

        while(self.stack2  and self.stack2[-1] <  val):

            pop = self.stack2.pop()

            self.stack3.append(pop)

        self.stack2.append(val)
        
        while(self.stack3):

            pop = self.stack3.pop()

            self.stack2.append(pop)
        

    def pop(self) -> None:

        val = self.stack1.pop()

        while(self.stack2[-1] !=  val):

            pop = self.stack2.pop()

            self.stack3.append(pop)

        self.stack2.pop()
        
        while(self.stack3):

            pop = self.stack3.pop()

            self.stack2.append(pop)
        

    def top(self) -> int:

        return self.stack1[-1]
        

    def getMin(self) -> int:

        return self.stack2[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()