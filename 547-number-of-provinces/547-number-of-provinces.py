class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        queue = deque([])
        count = 0
        
        def bfs(r):
            queue.append(r)
            while queue:
                row = queue.popleft()
                j = 0
                while j < len(isConnected):
                    if j not in visited and isConnected[row][j] == 1:
                        visited.add(j)
                        queue.append(j)
                    j += 1
        
        for i in range(len(isConnected)):
            if i not in visited:
                count += 1
                visited.add(i)
                bfs(i)
                
        return count
                                        
        
        
        