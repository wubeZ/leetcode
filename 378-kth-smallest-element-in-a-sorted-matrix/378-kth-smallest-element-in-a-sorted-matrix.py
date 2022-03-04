class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ans = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                val = -matrix[i][j]
                if len(ans) < k:
                    heapq.heappush(ans, val)
                    
                elif ans[0] < val:
                    heapq.heappop(ans)
                    heapq.heappush(ans, val)
                    
        return -ans[0]