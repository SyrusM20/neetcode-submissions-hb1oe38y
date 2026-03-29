class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bro = collections.defaultdict(list)
        for s in strs:
            sortedS = "".join(sorted(s))
            bro[sortedS].append(s)
        return list(bro.values())
