class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        graph = defaultdict(set)
        node1map = defaultdict(int)
        node2map = defaultdict(int)
        
        node1map[node1] = 0
        node2map[node2] = 0 
        
        n = len(edges)
        for src, des in enumerate(edges):
            if des != -1:
                graph[src].add(des)
        
        def findDist(node, dist_map):
            queue = deque()    
            queue.append((node,0))
            visited =set()
            visited.add(node)
            
            while queue:
                curnode, dist = queue.popleft()
                for nextnode in graph[curnode]:
                    if nextnode not in visited:
                        if dist_map[nextnode] != 0:
                            dist_map[nextnode] = min(dist_map[nextnode], dist + 1)
                        else:
                            dist_map[nextnode] = dist + 1
                        visited.add(nextnode)
                        queue.append((nextnode, dist + 1))
        
        findDist(node1, node1map)
        findDist(node2, node2map)
        
        ans = float("inf")
        maxx = float("inf")
        for node in range(n):
            if node in node1map and node in node2map:
                max_distance = max(node1map[node], node2map[node])
                if max_distance < maxx:
                    ans = node
                    maxx = max_distance    
                    
        if ans == float("inf"):
            return -1
        
        return ans
            