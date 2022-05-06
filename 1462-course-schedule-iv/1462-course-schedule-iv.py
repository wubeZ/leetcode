class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        
        for i,j in prerequisites:
            graph[i].append(j)
            
        @lru_cache(None)
        def dfs(start, end):
            if end in graph[start]:
                return True
            
            for j in graph[start]:
                if dfs(j, end):
                    return True
                    
            return False
            
        ans = []
        for i,j in queries:
            if dfs(i,j):
                ans.append(True)
            else:
                ans.append(False)
                
        return ans
        