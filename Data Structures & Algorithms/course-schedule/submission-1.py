class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:        
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        state = [0] * numCourses
        def dfs(crs):
            if state[crs] == 1:
                return False
            if state[crs] == 2:
                return True
            
            state[crs] = 1
            for nei in preMap[crs]:
                if not dfs(nei):
                    return False
            
            state[crs] = 2
            return True
        
        for crs in range(numCourses): # or preMap.keys()
            if not dfs(crs):
                return False
        return True
            
            
        

        