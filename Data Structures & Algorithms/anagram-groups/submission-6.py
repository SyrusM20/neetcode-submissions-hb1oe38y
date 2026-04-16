class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dic = collections.defaultdict(list)

        for s in strs:
            sortedS = "".join(sorted(s))
            my_dic[sortedS].append(s)
        
        return list(my_dic.values())