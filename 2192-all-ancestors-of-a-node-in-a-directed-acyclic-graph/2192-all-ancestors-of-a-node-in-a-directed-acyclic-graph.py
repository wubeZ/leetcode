class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indegree = [0] * n
        graph = [[] for i in range(n)] 
        queue = deque()
        res = [set() for i in range(n)]
        
        for i,j in edges:
            indegree[j] += 1
            graph[i].append(j)
            res[j].add(i)
        
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            cur = queue.popleft()
            ans = set()
            for i in res[cur]:
                ans.update(res[i])
            res[cur].update(ans)
        
            for i in graph[cur]:           
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
                    
        res = [sorted(ansestor) for ansestor in res]
        
        return res