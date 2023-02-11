class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        adjlist = defaultdict(deque)
        visited = set()
        for i,v in redEdges:
            adjlist[i].append((v,"R"))
            if i == 0:
                visited.add((v, "R"))
        for i,v in blueEdges:
            adjlist[i].append((v,"B"))
            if i == 0:
                visited.add((v, "B"))
        
        def bfs(target):
            queue = deque()
            seen = set()
            queue = adjlist[0].copy()
            seen = visited.copy()
            level = 0
            
            while queue:
                size = len(queue)
                level += 1
                for i in range(size):
                    cur_node, color = queue.popleft()
                    
                    if cur_node == target:
                        return level
                        
                    for next_node, next_color in adjlist[cur_node]:
                        if color != next_color and (next_node, next_color) not in seen:
                            queue.append((next_node, next_color))
                            seen.add((next_node, next_color))
                
            return -1
            
        ans = [0]
        for i in range(1,n):
            blueval = bfs(i)
            redval = bfs(i)
            
            if blueval == -1 or redval == -1:
                res = max(blueval, redval)
            else:
                res = min(blueval, redval)
            ans.append(res)
        
        return ans