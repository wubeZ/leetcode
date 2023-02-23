class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        heap = []
        
        projects = list(zip(capital, profits))
        projects.sort()
        
        left = 0
        
        for i in range(k):
            while left < len(projects) and projects[left][0] <= w:
                heapq.heappush(heap, -1 * projects[left][1])
                left += 1
            
            if heap:
                w -= heapq.heappop(heap)
        
        return w
        