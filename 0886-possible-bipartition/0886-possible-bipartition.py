class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adjlist = defaultdict(list)
        color = [0 for i in range(n + 1)]
        for src, dest in dislikes:
            adjlist[src].append(dest)
            adjlist[dest].append(src)
        
        visited = set()
        queue = deque()
        c = 1
        for i in range(1, n + 1):
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
                    for nxt in adjlist[cur]:
                        if nxt not in visited:
                            queue.append(nxt)
                            visited.add(nxt)
                        else:
                            if color[nxt] == c:
                                return False
                c = -c
        return True