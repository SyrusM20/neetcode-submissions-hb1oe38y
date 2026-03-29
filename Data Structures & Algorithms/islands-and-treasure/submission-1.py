class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()
        INF = 2147483647

        def addCell(r, c):
            if (r >= ROWS or c >= COLS or r < 0 or c < 0 or
                (r,c) in visit or grid[r][c] != INF):
                return
            
            q.append((r,c))
            visit.add((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = dist
                addCell(row + 1, col)
                addCell(row -1, col)
                addCell(row, col + 1)
                addCell(row, col - 1)
            dist += 1
