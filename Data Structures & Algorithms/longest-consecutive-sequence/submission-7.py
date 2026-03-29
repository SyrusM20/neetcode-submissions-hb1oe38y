class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in numSet:
            length = 0
            if num - 1 not in numSet:
                curr = num
                length += 1
                while curr + 1 in numSet:
                    length += 1
                    curr += 1
                longest = max(longest, length)
        return longest