class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = collections.defaultdict(list)

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([cost, j])
                adj[j].append([cost, i])  

        res = 0
        minHeap = [[0,0]]
        visit = set()
        while len(visit) < len(points):
            cost, point = heapq.heappop(minHeap)
            if point in visit:
                continue
            visit.add(point)
            res += cost

            for neiCost, nei in adj[point]:
                heapq.heappush(minHeap, [neiCost, nei])
        return res
        