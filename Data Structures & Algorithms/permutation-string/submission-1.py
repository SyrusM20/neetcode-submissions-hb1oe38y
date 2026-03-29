class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = {}
        for c in s1:
            need[c] = need.get(c, 0) + 1
        
        s2_counts = {}
        l = 0
        for r, ch in enumerate(s2):
            s2_counts[ch] = s2_counts.get(ch, 0) + 1

            while r - l + 1 > len(s1):
                s2_counts[s2[l]] -= 1
                if s2_counts[s2[l]] == 0:
                    del s2_counts[s2[l]]
                l += 1

            if need == s2_counts:
                return True
        return False