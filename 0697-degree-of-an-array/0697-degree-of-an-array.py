class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        dictionary = defaultdict(list)
        maxCount = 1
        ans = float("inf")
        
        for i in range(len(nums)):
            
            dictionary[nums[i]].append(i)
            
            if len(dictionary[nums[i]]) > maxCount:
                ans = float("inf")
            if len(dictionary[nums[i]]) >= maxCount:
                maxCount = len(dictionary[nums[i]])
                ans = min(ans, dictionary[nums[i]][-1] - dictionary[nums[i]][0] + 1)
                
        return ans
        
            