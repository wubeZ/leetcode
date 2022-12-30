class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        
        def backtrack(node, path):
            if node == (n - 1):
                ans.append(path[:])
                return
            
            for childnode in graph[node]:
                backtrack(childnode, path + [childnode])
            
            
        ans = []
        
        backtrack(0, [0])
        
        return ans