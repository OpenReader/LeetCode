class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_h = []
        self.max_h = []

    def addNum(self, num: int) -> None:
        if not self.max_h:
            heappush(self.max_h, -num)
            return
        
        top_num = -self.max_h[0]    
        if num > top_num: # go to right part
            heappush(self.min_h, num)
        else:
            heappush(self.max_h, -num)
        if len(self.min_h) > len(self.max_h):
            heappush(self.max_h, -heappop(self.min_h))
        elif len(self.min_h)+1 < len(self.max_h):
            heappush(self.min_h, -heappop(self.max_h))
        

    def findMedian(self) -> float:
        if not self.max_h:
            return None
        if len(self.min_h) == len(self.max_h):
            return (self.min_h[0] - self.max_h[0]) / 2
        return -self.max_h[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()