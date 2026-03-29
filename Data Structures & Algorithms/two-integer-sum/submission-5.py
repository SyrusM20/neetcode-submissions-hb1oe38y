class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numSet = {}
        for i, x in enumerate(nums): 
            need = target - x
            if need in numSet:
                return [numSet[need], i]
            numSet[x] = i