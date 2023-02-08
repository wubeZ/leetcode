class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        
        for i in range(len(equations)):
            a, b = equations[i]
            val = values[i]
            graph[a].append((b, val))
            graph[b].append((a, 1/val))
        
        
        def bfs(start, end):
            queue = deque()
            queue.append((start, 1))
            visited = set([start])
            
            if (start not in graph) or (end not in graph):
                return -1
            
            while queue:    
                cur_node, cur_value = queue.popleft()
                
                if cur_node == end:
                    return cur_value 
                
                for next_node, next_value in graph[cur_node]:
                    if next_node not in visited:
                        visited.add(next_node)
                        queue.append((next_node, cur_value * next_value))
            
            return -1
            
                    
        ans = []
        for start ,end in queries:
            temp = bfs(start, end)
            ans.append(temp)
            
        return ans
            