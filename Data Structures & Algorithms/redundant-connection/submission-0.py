class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = {i: [] for i in range(1, n + 1)}


        def dfs(curr, target, visited):
            if curr == target:
                return True
            visited.add(curr)
            for nei in adj[curr]:
                if nei not in visited:
                    if dfs(nei, target, visited):
                        return True
            return False

        for u, v in edges:
            visited = set()
            if adj[u] and adj[v] and dfs(u, v, visited):
                return [u, v]
            adj[u].append(v)
            adj[v].append(u)

        return []
        
        
