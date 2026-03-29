class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxF = res = l = 0
        counts = {}
        for r, ch in enumerate(s):
            counts[ch] = counts.get(ch, 0) + 1
            maxF = max(maxF, counts[ch])

            while (r - l + 1) - maxF > k:
                counts[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res