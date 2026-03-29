class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        res = ""
        for i, ch in enumerate(first):
            for s in strs[1:]:
                if  i == len(s) or s[i] != ch:
                    return res
            res += ch
        return res