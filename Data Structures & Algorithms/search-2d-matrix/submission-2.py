class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l, r = 0, (rows * cols) - 1

        # we flatten the 2D matrix by finding what row we land on, and using the remainder
        # to find how far into that row mid is at
        while l <= r:
            mid = (l + r) // 2
            row = mid // cols 
            col = mid % cols

            if matrix[row][col] < target:
                l = mid + 1
            elif matrix[row][col] > target:
                r = mid - 1
            else:
                return True
        return False