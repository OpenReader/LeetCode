class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.tensor = v
        self.outer_len = len(v)
        self.has_next = True
        if self.outer_len == 0:
            self.has_next = False
        else:
            self.outer_iter = -1
            self.outerNext()
    
    def outerNext(self):
        self.outer_iter += 1
        while self.outer_iter < self.outer_len and len(self.tensor[self.outer_iter]) == 0:
            self.outer_iter += 1
        if self.outer_iter == self.outer_len:
            self.has_next = False
        else:
            self.inner_iter = 0
            self.inner_len = len(self.tensor[self.outer_iter])
    
    def next(self) -> int:
        # print(self.outer_iter, self.inner_iter, self.inner_len)
        ret = self.tensor[self.outer_iter][self.inner_iter]
        self.inner_iter += 1
        if self.inner_iter == self.inner_len:
            self.outerNext()
        
        return ret

    def hasNext(self) -> bool:
        return self.has_next

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()