class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False

        freq1 = [0] * 26
        freqW = [0] * 26

        # Build first window
        for i in range(m):
            freq1[ord(s1[i]) - ord('a')] += 1
            freqW[ord(s2[i]) - ord('a')] += 1
        
        if freq1 == freqW:
            return True

        l = 0
        # Slide window
        for r in range(m, n):
            freqW[ord(s2[r]) - ord('a')] += 1 #incoming
            freqW[ord(s2[r - m]) - ord('a')] -= 1 # outgoing

            if freq1 == freqW:
                return True
        return False


