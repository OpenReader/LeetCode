class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        
        def getRows():
            rows = []
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        rows.append(i)
            return rows
        
        def getCols():
            cols = []
            for j in range(n):
                for i in range(m):
                    if grid[i][j] == 1:
                        cols.append(j)
            return cols
        
        def miniDistance1D(nums):
            dist = 0
            i, j = 0, len(nums) - 1
            while i < j:
                dist += nums[j] - nums[i]
                i += 1
                j -= 1
            return dist
        
        rows = getRows()
        cols = getCols()
        
        return miniDistance1D(rows) + miniDistance1D(cols)