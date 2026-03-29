class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t = list(t)
        for c in s:
            found = False
            for i in range(len(t)):
                if t[i] == c:
                    found = True
                    t.pop(i)
                    break
            if not found:
                return False
        if len(t) != 0:
            return False
        return True
            