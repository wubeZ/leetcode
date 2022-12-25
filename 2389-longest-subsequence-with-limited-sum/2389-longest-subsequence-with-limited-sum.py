class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = [0]
        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i])
        prefix = prefix[1:]
    
        ans = []
        for num in queries:
            val = bisect.bisect_right(prefix, num)
            ans.append(val)
        
        return ans