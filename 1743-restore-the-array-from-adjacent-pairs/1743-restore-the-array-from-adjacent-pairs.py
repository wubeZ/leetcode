class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for i, j in adjacentPairs:
            graph[i].append(j)
            graph[j].append(i)
        
        for node in graph:
            if len(graph[node]) == 1:
                start = node
        ans = [start]
        stack = [start]
        visited = set([start])
        
        while stack:
            
            cur_node = stack.pop()
            
            for next_node in graph[cur_node]:
                if next_node not in visited:
                    visited.add(next_node)
                    ans.append(next_node)
                    stack.append(next_node)
        
        return ans
        