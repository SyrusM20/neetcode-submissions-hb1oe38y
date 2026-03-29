class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit = set()  

        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)
            for j in adj[node]:
                if j == prev:
                    continue
                if not dfs(j, node) : return False
            return True
        return dfs(0, -1) and n == len(visit)