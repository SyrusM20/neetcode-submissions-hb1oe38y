class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""

        for c in s:
            if c.isalnum():
                newS += c.lower()
        if newS == newS[::-1]:
            return True
        return False
