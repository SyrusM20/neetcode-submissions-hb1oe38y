class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visit = set()
        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visit.add((r,c))
            perimeter = 0
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or
                        grid[nr][nc] == 0 ):
                        perimeter += 1
                    
                    elif (nr, nc) not in visit:
                        visit.add((nr,nc))
                        q.append((nr, nc))
            return perimeter
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return bfs(r,c)
        return 0