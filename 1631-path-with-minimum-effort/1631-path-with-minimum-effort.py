class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])
        directions = [[-1,0],[0,-1],[1,0],[0,1]]
        inbound = lambda x, y : 0 <= x < n and 0 <= y < m
        seen = set()
        heap = []
        heapq.heappush(heap, [0,0,0])
        dist = [ [float('inf') for j in range(m)] for i in range(n)]
        
        while heap:
            d, r, c = heapq.heappop(heap)
            
            if (r,c) in seen:
                continue
                
            seen.add((r,c))
            for rx, cy in directions:
                nr, nc = r + rx, c + cy
                if inbound(nr, nc):
                    effort = abs( heights[r][c] - heights[nr][nc])
                    if effort < dist[nr][nc]:
                        dist[nr][nc] = max(effort, d)
                        heapq.heappush(heap, [dist[nr][nc], nr, nc])
        
    
        return dist[n - 1][m - 1] if dist[n - 1][m - 1] != float("inf") else 0
        
        