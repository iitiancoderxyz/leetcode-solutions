class MyCircularQueue:

    def __init__(self, k: int):
        self.l=[None]*k
        self.k=k
        self.f=0
        self.size=0
    def enQueue(self, value: int) -> bool:
        if (self.size)==self.k:
            return False
        i=(self.f+self.size)%len(self.l)
        self.l[i]=value
        self.size+=1
        return True
    def deQueue(self) -> bool:
        if self.size==0:
            return False
        self.l[self.f]=None
        self.f=(self.f+1)%len(self.l)
        self.size-=1
        return True
    def Front(self) -> int:
        if self.size==0:
            return -1
        return self.l[self.f]

    def Rear(self) -> int:
        if self.size==0:
            return -1
        return self.l[(self.f+self.size-1)%len(self.l)]

    def isEmpty(self) -> bool:
        return self.size==0

    def isFull(self) -> bool:
        return self.size==len(self.l)
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()