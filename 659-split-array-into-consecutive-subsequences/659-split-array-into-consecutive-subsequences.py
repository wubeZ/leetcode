class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        vals = defaultdict(list)
        heapq.heappush(vals[nums[0]], 1)
        
        for i in range(1, len(nums)):
            if vals[nums[i] - 1]:
                temp = heapq.heappop(vals[nums[i] - 1])
                heapq.heappush(vals[nums[i]], temp + 1)
            else:
                heapq.heappush(vals[nums[i]], 1)

        for val in vals:
            temp = vals[val]
            if not all([x >= 3 for x in temp]):
                return False
            
        return True
                
        
                    