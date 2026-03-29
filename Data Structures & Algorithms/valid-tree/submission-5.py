class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit = set()
        def dfs(node, parent):
            if node in visit:
                return False
            
            visit.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        if not dfs(0,-1):
            return False
        return len(visit) == n
        






