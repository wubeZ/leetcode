class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        
        graph = defaultdict(list)
        
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)
            
        
        def dfs(node, parent):
             
            count = 1
            for next_node in graph[node]:
                if parent != next_node:
                    count += dfs(next_node, node)
                
            if node != 0:
                ans[0] += math.ceil(count / seats)
            
            return count
        
        
        ans = [0]
        
        dfs(0, -1)
        
        return ans[0]