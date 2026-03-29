class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for c in s:
            if c in pairs:
                stack.append(pairs[c])
            elif stack and stack[-1] == c:
                stack.pop()
            else:
                return False
        return not stack
        