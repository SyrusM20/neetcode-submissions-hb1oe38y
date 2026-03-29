class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            euclid_dist = (x*x) + (y*y)
            heapq.heappush(heap, (-euclid_dist, [x,y]))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [coords for _, coords in heap]