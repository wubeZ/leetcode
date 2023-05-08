class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for a, b in richer:
            graph[a].append(b)
            indegree[b] += 1
        
        queue = deque()
        ans = [i for i in range(len(quiet))]
        
        for i in range(len(quiet)):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue: 
            node = queue.popleft()
            
            for next_node in graph[node]:
                indegree[next_node] -= 1
                
                if quiet[ans[next_node]] > quiet[ans[node]]:
                    ans[next_node] = ans[node]
                
                if indegree[next_node] == 0:
                    # del indegree[next_node]
                    queue.append(next_node)
                    
        
        
        return ans