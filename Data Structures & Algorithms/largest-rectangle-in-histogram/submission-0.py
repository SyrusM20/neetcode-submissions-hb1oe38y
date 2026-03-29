class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        heights.append(0)               # A guaranteed right boundary for any  values that dont -> 
        for i, h in enumerate(heights): # -> run into that right bound ex. [1,2,3,4]
            while stack and heights[stack[-1]] > heights[i]:
                mid = stack.pop()
                height = heights[mid]
                right = i
                left = stack[-1] if stack else -1
                width = right - left - 1 # since bounds aren't included
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area