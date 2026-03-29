class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        q = deque()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        pac = [[False] * COLS for _ in range(ROWS)]
        atl = [[False] * COLS for _ in range(ROWS)]

        def bfs(q, ocean):
            while q:
                row, col = q.popleft()
                ocean[row][col] = True
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or
                         ocean[nr][nc] != False or heights[nr][nc] < heights[row][col]):
                        continue
                    q.append((nr,nc))

        q_pac = deque()
        q_atl = deque()

        for c in range(COLS):
            q_pac.append((0, c))
            q_atl.append((ROWS - 1, c))
        
        for r in range(ROWS):
            q_pac.append((r, 0))
            q_atl.append((r, COLS - 1))

        bfs(q_pac, pac)
        bfs(q_atl, atl)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c] == True:
                    res.append([r,c])
        return res

        
        


