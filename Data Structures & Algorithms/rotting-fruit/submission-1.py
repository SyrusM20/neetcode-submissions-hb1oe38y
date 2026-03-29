class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1

        def addCell(r, c):
            nonlocal fresh, rotted
            if (r >= ROWS or c >= COLS or r < 0 or c < 0 or
                (r,c) in visit or grid[r][c] != 1):
                return
            q.append((r,c))
            visit.add((r,c))
            fresh -= 1
            grid[r][c] = 2
            rotted = True

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visit.add((r,c))
        mins = 0
        while q:
            rotted = False
            for i in range(len(q)):
                row, col = q.popleft()
                addCell(row + 1, col)
                addCell(row - 1, col)
                addCell(row, col + 1)
                addCell(row, col - 1)
            if rotted:
                mins += 1

        return -1 if fresh > 0 else mins

        
        
