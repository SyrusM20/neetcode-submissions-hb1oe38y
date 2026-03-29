class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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
        
        counter = 0
        for node in range(n):
            if node not in visit:
                dfs(node)
                counter += 1
        return counter