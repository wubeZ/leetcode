class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        
        for i in range(len(roads)):
            graph[roads[i][0]].append([roads[i][1],roads[i][2]])
            graph[roads[i][1]].append([roads[i][0],roads[i][2]])
        
        ans = float("inf")
        queue = deque([1])
        seen = set([1])
    
        while queue:
            node = queue.popleft()
            
            for child, dis in graph[node]:
                ans = min(ans, dis)
                
                if child not in seen:
                    queue.append(child)
                    seen.add(child)
        
        return ans