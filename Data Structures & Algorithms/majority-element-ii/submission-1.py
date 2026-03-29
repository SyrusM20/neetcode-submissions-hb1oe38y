class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numCounts = {}
        for num in nums:
            numCounts[num] = numCounts.get(num, 0) + 1

        res = []
        for num, cnt in numCounts.items():
            if cnt > len(nums) // 3:
                res.append(num)
        return res if len(res) > 0 else []