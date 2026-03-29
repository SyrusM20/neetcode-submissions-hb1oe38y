class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)

        for src, dest in tickets:
            adj[src].append(dest)
        
        for src in adj:
            adj[src].sort(reverse=True)

        route = []
        def dfs(src):
            while adj[src]:
                next = adj[src].pop()
                dfs(next)
            route.append(src)
        
        dfs("JFK")
        return route[::-1]