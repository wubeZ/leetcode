class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        if len(counter.keys()) < 3: return False
        dp = [1] * len(nums)
        
        for i in range(len(nums)-1,-1,-1):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
            if dp[i] >= 3:
                return True
        return False