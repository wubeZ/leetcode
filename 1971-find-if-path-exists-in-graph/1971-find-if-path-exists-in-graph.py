class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        queue = deque([source])
        visited = set()
        def bfs():
            while queue:
                n = len(queue)
                i = 0
                while i < n and queue:
                    cur = queue.popleft()
                    if cur in visited:
                        continue
                    visited.add(cur)
                    if cur == destination:
                        return True
        
                    for i in range(len(edges)):
                        if cur == edges[i][0] :
                            queue.append(edges[i][1])
                        elif cur == edges[i][1]:
                            queue.append(edges[i][0])              
                    i+= 1
            return False
        
        return bfs()