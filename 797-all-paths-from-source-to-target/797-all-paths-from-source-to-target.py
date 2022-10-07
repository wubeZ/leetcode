class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        res = []
        
        queue = deque([[0, []]])
        
        while queue:
            cur, path = queue.popleft()
            if cur == len(graph)-1:
                res.append(path + [cur])
            
            for node in graph[cur]:
                queue.append([node, path + [cur]])
        
        return res