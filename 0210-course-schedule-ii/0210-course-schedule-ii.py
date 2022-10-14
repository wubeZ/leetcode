class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        color = defaultdict(int)
        adjlist = defaultdict(list)
        
        for i in range(len(prerequisites)):
            a, b = prerequisites[i]
            adjlist[b].append(a)
        
        topSortOrder = []
        
        def dfs(node):
            if color[node] == 1:
                return True
            if color[node] == 2:
                return False
            
            color[node] = 1
            
            for childNode in adjlist[node]:
                if dfs(childNode):
                    return True
            color[node] = 2
            topSortOrder.append(node)
            return False
        
        for i in range(numCourses):
            if dfs(i): return []
            
        return topSortOrder[::-1]