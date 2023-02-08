class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        graph = defaultdict(set)
        
        for idx, route in enumerate(routes):
            for bus in route:
                graph[bus].add(idx)
        
        queue = deque([(source, 0)])
        visited = set([source])
        seen_idx = set()
        
        while queue:
            cur_node, level = queue.popleft()
            if cur_node == target:
                return level
            
            for idx in graph[cur_node]:
                if idx not in seen_idx:
                    for next_node in routes[idx]: 
                        if next_node not in visited:
                            visited.add(next_node)
                            queue.append((next_node, level + 1))
                    seen_idx.add(idx)
        
        return -1