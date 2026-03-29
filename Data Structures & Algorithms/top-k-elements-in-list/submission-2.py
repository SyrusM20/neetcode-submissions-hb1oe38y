class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] = 1 + counts.get(num)
            else:
                counts[num] = 1
        arr = []
        for num, cnt in counts.items():
            arr.append([cnt,num])
        arr.sort()

        res = []
        for i in range(k):
            res.append(arr.pop()[1])
        return res


        