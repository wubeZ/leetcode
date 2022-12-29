class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        heap = []
        time = 0
        for i in range(len(tasks)):
            heapq.heappush(heap, (tasks[i][0], tasks[i][1], i))
        
        temp = heapq.heappop(heap)
        scheduler = [(temp[1], temp[2])]
        time = temp[0]
        ans = []
        
        while heap or len(scheduler) > 0:

            while heap and time >= heap[0][0]:
                temp = heapq.heappop(heap)
                heapq.heappush(scheduler, (temp[1],temp[2]))
            
            if scheduler:
                cur = heapq.heappop(scheduler)
                time += cur[0]
                ans.append(cur[1])
                time = max(time, cur[0])
            else:
                time = heap[0][0]

        
        return ans
        
        
            
        
        