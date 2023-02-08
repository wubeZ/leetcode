class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for i, j in adjacentPairs:
            graph[i].append(j)
            graph[j].append(i)
        
        for node in graph:
            if len(graph[node]) == 1:
                start = node
        
        visited = set()
        
        def dfs(node):

            for next_node in graph[node]:
                if next_node not in visited:
                    visited.add(next_node)
                    ans.append(next_node)
                    dfs(next_node)
            
        
        ans = [start]
        visited.add(start)
        dfs(start)
        
        return ans
        