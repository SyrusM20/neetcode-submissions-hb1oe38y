class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for x, y in points:
            euclid_dist = (x*x) + (y*y)
            heapq.heappush(heap, (euclid_dist, [x,y]))
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res