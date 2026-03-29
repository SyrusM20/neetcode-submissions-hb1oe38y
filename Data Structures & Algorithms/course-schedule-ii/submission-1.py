class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # [1,0],[2,0],[3,1],[3,2]
        # {0 = []
        #  1 = [0]
        #  2 = [0]
        #  3 = [1,2]}

        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        state = [0] * numCourses
        res = []
        def dfs(crs):
            if state[crs] == 1:
                state[crs] = 0
                return False
            if state[crs] == 2:
                return True
            
            state[crs] = 1
            for nei in preMap[crs]:
                if not dfs(nei):
                    return False
            state[crs] = 2
            res.append(crs)
            return True
        
        for crs in preMap.keys():
            if not dfs(crs):
                return []
        return res
        

