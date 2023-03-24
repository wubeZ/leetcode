class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(set)
        adjacency = defaultdict(list)
        
        for x, y in connections:
            graph[x].add(y)
            adjacency[x].append(y)
            adjacency[y].append(x)
        
        queue = deque()
        res = 0
        queue.append((0, 0))
        
        while queue:
            
            cur, parent = queue.popleft()
            
            for child in adjacency[cur]:
                if child == parent:
                    continue
                    
                if cur not in graph[child]:
                    res += 1
                        
                queue.append((child, cur))
        
        return res
            