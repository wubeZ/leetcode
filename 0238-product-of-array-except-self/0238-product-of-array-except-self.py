class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        backprefix = [1]
        for i in range(len(nums)):
            prefix.append(prefix[-1] * nums[i])
        for i in range(len(nums)-1,-1,-1):
            backprefix.append(backprefix[-1] * nums[i])
        backprefix = backprefix[::-1]
        
        ans = []
        for i in range(len(nums)):
            ans.append(prefix[i] * backprefix[i+1])
        
        return ans