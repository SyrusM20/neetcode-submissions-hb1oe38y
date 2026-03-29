class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()
        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for nei in adj[node]:
                dfs(nei)
        dfs(0)

        return len(visit) == n






