class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = {}
        window = {}
        for c in s1:
            freq_s1[c] = freq_s1.get(c, 0) + 1
        
        l = 0
        for r, ch in enumerate(s2):
            window[ch] = window.get(ch, 0) + 1

            while (r - l + 1) > len(s1):
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l += 1
            
            if freq_s1 == window:
                return True
        return False