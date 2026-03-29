class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        q = deque()

        for r in (0, ROWS - 1):
            for c in range(COLS):
                if board[r][c] == "O":
                    q.append((r,c))
        for c in (0, COLS - 1):
            for r in range(ROWS):
                if board[r][c] == "O":
                    q.append((r,c))
        
        while q:
            row, col = q.popleft()
            board[row][col] = "#"
            for dr, dc in directions:
                nr, nc = dr + row, dc + col
                if (0 <= nr < ROWS and 0 <= nc < COLS and
                    board[nr][nc] == "O"):
                    q.append((nr,nc))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"

