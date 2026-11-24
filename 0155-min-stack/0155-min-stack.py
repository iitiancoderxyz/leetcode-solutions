class MinStack:
    def __init__(self):
        self.l=[]
        self.m=[]
    def push(self, val: int) -> None:
        if len(self.m)==0:
            self.m.append(val)
        elif val<=self.m[-1]:
            self.m.append(val)
        self.l.append(val)
    def pop(self) -> None:
        if self.l[-1]==self.m[-1]:
            self.m.pop()
        self.l.pop()
    def top(self) -> int:
        return self.l[-1]    
    def getMin(self) -> int:
        return self.m[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()