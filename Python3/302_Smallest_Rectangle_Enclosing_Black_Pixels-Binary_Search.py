class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        
        def searchCols(low: int, high: int, left_part: bool) -> int:
            while low != high:
                k, mid = 0, low + (high - low) // 2
                while k < self.m and image[k][mid] == '0':
                    k += 1
                if (k < self.m) == left_part:
                    high = mid
                else:
                    low = mid + 1
            return high
        
        def searchRows(low: int, high: int, start: int, end: int, up_part: bool) -> int:
            while low != high:
                k, mid = start, low + (high - low) // 2
                while k < end and image[mid][k] == '0':
                    k += 1
                if (k < end) == up_part:
                    high = mid
                else:
                    low = mid + 1
            return high
        
        self.m = len(image)
        if self.m == 0:
            return 0
        self.n = len(image[0])
        
        left = searchCols(0, y, True)
        right = searchCols(y+1, self.n, False)
        top = searchRows(0, x, 0, self.n, True)
        bottom = searchRows(x+1, self.m, 0, self.n, False)
        
        # print(left, right, top, bottom)
        
        return (right - left) * (bottom - top)