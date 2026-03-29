class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # {0 : [1,2,3],
        #  1 : [0,4]
        #  2 : [0]
        #  3 : [0]
        #  4 : [1]}
        adj_list = collections.defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u) # since this is undirected, we add it both ways
        
        must_visit = len(edges)
        visit = set()
        def dfs(node, parent):
            visit.add(node)
            for nei in adj_list[node]:
                if nei == parent:
                    continue
                if nei in visit:
                    return False
                if not dfs(nei, node):
                    return False
            return True
        
        if not dfs(0,-1):
            return False
        return len(visit) == n

                



