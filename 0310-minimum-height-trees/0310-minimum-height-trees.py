class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        d = defaultdict(int)
        indegree = defaultdict(int)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] += 1
        
        queue = deque()
        seen = set()
        
        for key in indegree:
            if indegree[key] == 1:
                queue.append((key, 0))
                seen.add(key)
        ans = [0] * n
        while queue:

            cur,count = queue.popleft()

            for ne in graph[cur]:

                if ne == cur:
                    continue

                indegree[ne] -= 1
                
                count = max(count, ans[ne])

                if indegree[ne] == 1:
                    if ne not in seen:
                        queue.append((ne, count + 1))
                        seen.add(ne)
            ans[cur] = count
        
        
        res = []
        c = float("-inf")
        for i in range(len(ans)):
            if c == ans[i]:
                res.append(i)
            elif c < ans[i]:
                res = []
                c = ans[i]
                res.append(i)
                
        return res