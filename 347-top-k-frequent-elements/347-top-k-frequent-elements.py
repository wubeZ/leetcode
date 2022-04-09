class Solution(object):
    def topKFrequent(self, nums, k):
        heap = []
        counter = Counter(nums)
        ans = []
        for i in counter:
            heapq.heappush(heap, (-counter[i],i))
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
            
        return ans
        
        