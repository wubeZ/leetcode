class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0 for i in range(n)]        
        visited = set()
        queue = deque()
        c = 1
        for i in range(n):
            if i in visited:
                continue
            queue.append(i)
            visited.add(i)
            
            while queue:
                sz = len(queue)
                for j in range(sz):
                    cur = queue.popleft()
                    if color[cur] == -c:
                        return False
                    
                    color[cur] = c 
                    for nxt in graph[cur]:
                        if nxt not in visited:
                            queue.append(nxt)
                            visited.add(nxt)
                        else:
                            if color[nxt] == c:
                                return False
                c = -c
        return True