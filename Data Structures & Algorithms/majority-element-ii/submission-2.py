class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numCounts = {}
        for num in nums:
            numCounts[num] = numCounts.get(num,0) + 1

        n = len(nums)
        res = []
        for num, cnt in numCounts.items():
            if cnt >  (n // 3):
                res.append(num)

        return res