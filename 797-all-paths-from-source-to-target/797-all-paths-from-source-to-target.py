class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        self.ans = []
        def dfs(node,path):
            if node == len(graph)-1:
                self.ans.append(path + [node])
                return 
            for newNode in graph[node]:
                dfs(newNode, path + [node])

        dfs(0, [])
        
        return self.ans