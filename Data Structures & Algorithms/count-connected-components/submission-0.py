class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i : [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit = [False] * n
        
        def bfs(node):
            q = deque([node])
            while q:
                curr = q.popleft()
                for nei in adj[curr]:
                    if not visit[nei]:
                        visit[nei] = True
                        q.append(nei)
        res = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                bfs(node)
                res += 1
        return res

