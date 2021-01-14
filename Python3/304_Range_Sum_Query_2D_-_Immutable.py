class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        if n == 0:
            return
        self.acc = [[0] * n for _ in range(m)]
        self.acc[0][0] = matrix[0][0]
        # init first row
        for j in range(1, n):
            self.acc[0][j] = self.acc[0][j-1] + matrix[0][j]
        # init first col
        for i in range(1, m):
            self.acc[i][0] = self.acc[i-1][0] + matrix[i][0]
        
        for i in range(1, m):
            for j in range(1, n):
                self.acc[i][j] = matrix[i][j] + self.acc[i-1][j] + self.acc[i][j-1] - self.acc[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # print(self.acc[row2][col2])
        ret = self.acc[row2][col2]
        if row1 - 1 >= 0:
            ret -= self.acc[row1-1][col2]
        if col1 - 1 >= 0:
            ret -= self.acc[row2][col1-1]
        if row1 - 1 >= 0 and col1 - 1 >= 0:
            ret += self.acc[row1-1][col1-1]
        return ret


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)