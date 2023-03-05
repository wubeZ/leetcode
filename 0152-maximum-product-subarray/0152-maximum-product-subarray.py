class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        product_prefix = [1]
        product_suffix = [1]
        ans = float("-inf")
        
        for num in nums:
            if product_prefix[-1] == 0:
                product_prefix.append(num)
            else:
                product_prefix.append(product_prefix[-1] * num)
        
        for num in nums[::-1]:
            if product_suffix[-1] == 0:
                product_suffix.append(num)
            else:
                product_suffix.append(product_suffix[-1] * num)
        
        product_prefix = product_prefix[1:]
        product_suffix = product_suffix[1:]
        
        for i in range(len(nums)):
            ans = max(ans, product_prefix[i], product_suffix[i])
            
        return ans