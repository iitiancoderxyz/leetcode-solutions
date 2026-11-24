class MyStack:

    def __init__(self):
        self.value=deque()

    def push(self, x: int) -> None:
        self.value.append(x)
        for i in range(len(self.value)-1):
           self.value.append(self.value.popleft())
    def pop(self) -> int:
        x=self.value[0]
        self.value.popleft()
        return x        
    def top(self) -> int:
        return self.value[0]        

    def empty(self) -> bool:
        return len(self.value)==0        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()