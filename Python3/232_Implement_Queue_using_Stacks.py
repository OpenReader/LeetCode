class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.st1, self.st2 = [], []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.st1.append(x)
        
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.st2:
            return self.st2.pop()
        # if not self.st1:
        #     return None
        while self.st1:
            self.st2.append(self.st1.pop())
        return self.st2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.st2:
            return self.st2[-1]
        # if not self.st1:
        #     return None
        while self.st1:
            self.st2.append(self.st1.pop())
        return self.st2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not (self.st1 or self.st2)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()