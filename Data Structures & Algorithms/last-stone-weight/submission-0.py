class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-weight for weight in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first_heaviest = -heapq.heappop(heap)
            second_heaviest = -heapq.heappop(heap)

            if first_heaviest == second_heaviest:
                continue
            else:
                first_heaviest -= second_heaviest
                heapq.heappush(heap, -first_heaviest)
        
        return -heapq.heappop(heap) if heap else 0
