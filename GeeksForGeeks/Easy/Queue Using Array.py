# Chat GPT giải -> Chưa giải được
class myQueue:
    def __init__(self, n):
        self.n = n
        self.arr = [0] * n
        self.front = -1
        self.rear = -1

    def enqueue(self, x):
        if self.isFull():
            return
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.n
        self.arr[self.rear] = x

    def dequeue(self):
        if self.isEmpty():
            return
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.n

    def getFront(self):
        return -1 if self.isEmpty() else self.arr[self.front]

    def getRear(self):
        return -1 if self.isEmpty() else self.arr[self.rear]

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return (self.rear + 1) % self.n == self.front
