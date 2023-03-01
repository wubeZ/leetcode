class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        
        ans = []
        while nums:
            ans.append(heapq.heappop(nums))
            
        return ans