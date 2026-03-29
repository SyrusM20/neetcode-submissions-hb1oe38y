class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def backtrack(i):
            if i == len(s):
                res.append(path.copy())
                return
            
            for j in range(i, len(s)):
                piece = s[i:j+1]
                if piece == piece[::-1]:
                    path.append(piece)
                    backtrack(j + 1)
                    path.pop()
        backtrack(0)
        return res