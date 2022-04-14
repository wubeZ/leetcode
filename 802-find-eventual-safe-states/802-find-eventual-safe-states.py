class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        outdegree = [0] * len(graph)
        lists = defaultdict(list)
        queue, ans = deque(), []
        
        for i in range(len(graph)):
            outdegree[i] = len(graph[i])
            for j in range(len(graph[i])):
                lists[graph[i][j]].append(i)

        for i in range(len(outdegree)):
            if outdegree[i] == 0:
                queue.append(i)
        
        while queue:
            cur = queue.popleft()
            ans.append(cur)
            
            for n in lists[cur]:
                outdegree[n] -= 1
                if outdegree[n] == 0:
                    queue.append(n)
                    
        return sorted(ans)