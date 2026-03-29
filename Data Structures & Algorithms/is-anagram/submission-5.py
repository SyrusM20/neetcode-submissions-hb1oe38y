class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts_s = {}
        for letter in s:
            counts_s[letter] = counts_s.get(letter, 0) + 1
        
        for letter in t:
            if letter not in counts_s or counts_s[letter] == 0:
                return False
            counts_s[letter] -= 1
        return True

        
