class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        limit = len(nums)//2
        d = defaultdict(int)
        ans = 0
        for i in range(len(nums)):
            d[nums[i]] += 1
            if d[nums[i]] > limit:
                ans = nums[i]
        
        return ans