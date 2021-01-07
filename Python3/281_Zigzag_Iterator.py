class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v = [v1, v2]
        self.L = [len(v1), len(v2)]
        self.i, self.j = -1, 0
        self.max_l = max(self.L)
        self.v_left = 0
        for l in self.L:
            if l > 0:
                self.v_left += 1
        
    def next(self) -> int:
        self.i += 1
        while self.i < 2 and self.j >= self.L[self.i]:
            self.i += 1
        if self.i == 2:
            self.i, self.j = 0, self.j + 1
            while self.i < 2 and self.j >= self.L[self.i]:
                self.i += 1
        if self.j == self.L[self.i] - 1:
            self.v_left -= 1
        return self.v[self.i][self.j]
        
            

    def hasNext(self) -> bool:
        return False if self.v_left == 0 else True

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())