class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.queue = [-1] * self.k
        self.front = self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isEmpty():
            self.queue[self.rear] = value
            self.front = self.rear
        else:
            if self.isFull():
                return False
            else:
                self.rear = (self.rear + 1) % self.k
                self.queue[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.queue[self.front] = -1
            self.front = (self.front + 1) % self.k
            return True

    def Front(self) -> int:
        return self.queue[self.front]

    def Rear(self) -> int:
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.queue[self.front] == -1

    def isFull(self) -> bool:
        return (self.rear + 1) % self.k == self.front and self.queue[self.front] != -1

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()