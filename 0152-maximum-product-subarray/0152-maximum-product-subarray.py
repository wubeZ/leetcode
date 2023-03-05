class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pos_product = nums[0]
        neg_product = nums[0]
        
        ans = nums[0]
        
        for i in range(1, len(nums)):
            
            pos_temp = max(nums[i], pos_product*nums[i], neg_product*nums[i])
            neg_temp = min(nums[i], pos_product*nums[i], neg_product*nums[i])            
            
            pos_product = pos_temp
            neg_product = neg_temp
            
            ans = max(pos_product, ans)
            
        return ans