class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sortedS = "".join(sorted(s))
        sortedT = "".join(sorted(t))

        if sortedS == sortedT:
            return True
        return False