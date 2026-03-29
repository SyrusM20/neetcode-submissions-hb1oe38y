class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])

        pre = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(1, rows + 1):
            row_sum = 0
            for c in range(1, cols + 1):
                row_sum += matrix[r - 1][c - 1]
                pre[r][c] = pre[r-1][c] + row_sum
        self.pre = pre

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        pre = self.pre

        r1 = row1
        c1 = col1
        r2 = row2 + 1
        c2 = col2 + 1
        return pre[r2][c2] - pre[r1][c2] - pre[r2][c1] + pre[r1][c1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)