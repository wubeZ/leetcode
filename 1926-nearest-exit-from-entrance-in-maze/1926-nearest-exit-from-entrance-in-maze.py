class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        inbound = lambda x, y: 0 <= x < len(maze) and 0 <= y < len(maze[0])
        count = 0
        q = deque()
        visited = set()
        q.append((entrance[0],entrance[1]))
        visited.add((entrance[0], entrance[1]))
        
        while q:
            temp = deque()
            while q:
                r,c = q.popleft()

                for dx, dy in direction:
                    nr, nc = r + dx, c + dy
                    if not inbound(nr,nc) and [r,c] != entrance:
                        return count
                    if inbound(nr,nc) and maze[nr][nc] != "+" and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        temp.append((nr, nc))
            q = temp
            count += 1
        return -1
            